---
name: github-actions-workflow
description: >
  Tạo và tối ưu hóa GitHub Actions workflows. Sử dụng khi làm việc với CI/CD,
  GitHub Actions, workflow YAML, automation, testing pipelines, deployment workflows,
  hoặc khi cần tạo, sửa, review, hoặc debug các file workflow .yml/.yaml trong
  .github/workflows/. Bao gồm cả việc thiết lập jobs, steps, triggers, caching,
  secrets, matrix builds, reusable workflows, và security best practices.
---

# GitHub Actions Workflow

Tạo workflows GitHub Actions production-ready với cấu trúc rõ ràng, bảo mật cao, và hiệu suất tối ưu.

## Cấu trúc workflow cơ bản

Mọi workflow được lưu trong `.github/workflows/` với định dạng YAML:

```yaml
name: Workflow Name

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  job-name:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      - name: Run tests
        run: npm test
```

## Nguyên tắc thiết kế

### Bảo mật là ưu tiên hàng đầu

**Pin actions bằng commit SHA**, không dùng tags hoặc branches vì chúng có thể bị thay đổi:

```yaml
# Tránh
- uses: actions/checkout@v4

# Nên dùng
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
```

**Permissions theo nguyên tắc least privilege**:

```yaml
permissions:
  contents: read

jobs:
  deploy:
    permissions:
      contents: read
      deployments: write
```

**Tránh script injection** từ user input:

```yaml
# Nguy hiểm - PR title có thể chứa malicious commands
- run: echo "PR: ${{ github.event.pull_request.title }}"

# An toàn - dùng environment variable
- name: Print PR title
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
  run: echo "PR: $PR_TITLE"
```

### Chia nhỏ workflows

Thay vì một file khổng lồ, tạo nhiều workflows nhỏ tập trung:

- `ci.yml` - lint và test
- `deploy.yml` - deployment
- `scheduled.yml` - scheduled tasks
- `release.yml` - release automation

Dùng **reusable workflows** cho logic dùng chung:

```yaml
# .github/workflows/reusable-test.yml
on:
  workflow_call:
    inputs:
      node-version:
        required: true
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
      - run: npm test
```

Gọi từ workflow khác:

```yaml
jobs:
  test:
    uses: ./.github/workflows/reusable-test.yml
    with:
      node-version: '20'
```

### Timeout và concurrency

**Luôn set timeout** để tránh lãng phí runner minutes:

```yaml
jobs:
  test:
    timeout-minutes: 30  # Default là 6 giờ - quá dài!
```

**Dùng concurrency** để cancel các runs cũ:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

## Triggers và filters

### Path filters cho monorepos

```yaml
on:
  push:
    paths:
      - 'services/api/**'
      - '!services/api/docs/**'
```

### Conditional execution

```yaml
jobs:
  deploy:
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
```

### Scheduled workflows với timezone (2026+)

```yaml
on:
  schedule:
    - cron: '30 9 * * 1-5'
      timezone: 'America/New_York'
```

## Caching và optimization

**Cache dependencies** để tăng tốc:

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

**Matrix builds** cho multi-version testing:

```yaml
strategy:
  matrix:
    node-version: [18, 20, 22]
    os: [ubuntu-latest, windows-latest]
  fail-fast: false

runs-on: ${{ matrix.os }}
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: ${{ matrix.node-version }}
```

## Secrets và environments

**Dùng GitHub Secrets** cho sensitive data:

```yaml
steps:
  - name: Deploy
    env:
      API_KEY: ${{ secrets.API_KEY }}
    run: ./deploy.sh
```

**Environment-specific secrets** với protection rules:

```yaml
jobs:
  deploy:
    environment:
      name: production
      url: https://example.com
    steps:
      - name: Deploy to prod
        env:
          DEPLOY_TOKEN: ${{ secrets.PROD_DEPLOY_TOKEN }}
        run: ./deploy.sh
```

Để dùng environment mà không tạo deployment (2026+):

```yaml
jobs:
  test:
    environment:
      name: staging
      deployment: false
```

## Service containers

Chạy databases hoặc services cho testing:

```yaml
services:
  postgres:
    image: postgres:15
    env:
      POSTGRES_PASSWORD: postgres
    options: >-
      --health-cmd pg_isready
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5
    ports:
      - 5432:5432
```

Override entrypoint/command (2026+):

```yaml
services:
  redis:
    image: redis:7
    entrypoint: redis-server
    command: --maxmemory 256mb
```

## Debugging

**Debug logging**: Re-run workflow với "Enable debug logging" hoặc set secret `ACTIONS_STEP_DEBUG=true`.

**Step outputs** để debug giá trị:

```yaml
- name: Check value
  id: check
  run: echo "result=success" >> $GITHUB_OUTPUT

- name: Use output
  run: echo "Result was ${{ steps.check.outputs.result }}"
```

## Anti-patterns cần tránh

❌ Dùng mutable references (tags/branches) cho actions  
❌ Để permissions mặc định (quá rộng)  
❌ Không set timeout  
❌ Hardcode secrets trong workflow  
❌ Chạy workflows không cần thiết trên mọi commit  
❌ Inline bash scripts dài - nên tách ra `scripts/`  

## Checklist review workflow

- [ ] Actions được pin bằng commit SHA với comment version
- [ ] Permissions set theo least privilege
- [ ] Timeout được set hợp lý (< 30 phút cho hầu hết workflows)
- [ ] Concurrency được cấu hình nếu cần
- [ ] Secrets không bao giờ được print ra logs
- [ ] Path/branch filters được dùng để tránh unnecessary runs
- [ ] Cache được cấu hình cho dependencies
- [ ] Job và step names rõ ràng, mô tả
- [ ] Conditional logic dùng `if` thay vì nested workflows
- [ ] Reusable workflows được dùng cho logic lặp lại

## Ví dụ: Complete CI/CD workflow

```yaml
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
      
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - run: npm ci
      - run: npm run lint
      - run: npm test
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        if: always()

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    timeout-minutes: 15
    environment:
      name: production
      url: https://example.com
    permissions:
      contents: read
      deployments: write
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
      
      - name: Deploy
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
        run: ./scripts/deploy.sh
```

Workflow này minh họa: security best practices, proper permissions, caching, conditional deployment, và clear structure.