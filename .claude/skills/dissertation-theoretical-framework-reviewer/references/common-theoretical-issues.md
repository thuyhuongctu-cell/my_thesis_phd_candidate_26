# Common Theoretical Issues in I-P Dissertations

This reference catalogs frequent problems encountered in internationalization-performance dissertation theoretical frameworks, with guidance on how to identify and fix them.

## Issue Category 1: Theory Integration Problems

### Problem 1.1: "Christmas Tree" Syndrome

**Description**: Listing multiple theories without explaining how they fit together.

**Example**:
> "This study draws on Resource-Based View, Institutional Theory, Transaction Cost Economics, Agency Theory, Organizational Learning Theory, and Network Theory to examine..."

**Why it's problematic**:
- Too many theories dilute focus
- No clear logic for why each is needed
- Theories may contradict each other
- Impossible to test all implications

**How to fix**:
1. Identify 2-4 core theories maximum
2. Explain the specific role of each theory (e.g., "RBV explains firm heterogeneity, Institutional Theory explains country heterogeneity")
3. Show how theories complement rather than compete
4. Map each hypothesis to its theoretical foundation

**Good example**:
> "We integrate three theories in a layered framework: (1) Uppsala Model provides the process foundation for learning costs, (2) RBV explains why firms with superior capabilities achieve better I-P outcomes, and (3) Institutional Theory specifies how home-country context moderates both the learning process and capability deployment."

---

### Problem 1.2: Theory-Hypothesis Mismatch

**Description**: Hypotheses don't actually follow from the theories invoked.

**Example**:
> "Drawing on Institutional Theory, we hypothesize that firms with higher R&D intensity will achieve better internationalization performance (H1)."

**Why it's problematic**:
- R&D intensity is a firm-level resource (RBV), not an institutional variable
- Institutional Theory explains country-level or cross-country effects
- Reviewers will immediately spot the disconnect

**How to fix**:
1. For each hypothesis, explicitly state: "From [Theory X], we derive that [mechanism Y] leads to [outcome Z]"
2. Check that the level of analysis matches (firm-level theory → firm-level hypothesis)
3. Ensure the mechanism invoked is actually part of the theory

**Good example**:
> "Drawing on Institutional Theory (Khanna & Palepu, 2010), we argue that institutional voids in the home country increase transaction costs for internationalizing firms. However, firms that develop capabilities to navigate these voids (Cuervo-Cazurra et al., 2018) can transfer these capabilities to similarly challenging foreign markets. Therefore, we hypothesize that home-country institutional obstacles negatively moderate the I-P relationship for firms with low digital capabilities, but this negative effect is attenuated for firms with high digital capabilities that can bypass traditional institutional intermediaries (H5)."

---

### Problem 1.3: Missing Mechanism

**Description**: Stating a relationship without explaining the causal process.

**Example**:
> "We hypothesize that internationalization is positively related to firm performance (H1)."

**Why it's problematic**:
- No explanation of *why* or *how* the relationship exists
- Could be driven by multiple mechanisms (economies of scale? learning? diversification?)
- Impossible to design proper empirical test without knowing mechanism

**How to fix**:
1. Always include "because" or "through" in hypothesis development
2. Specify the mediating process
3. Distinguish your mechanism from alternative mechanisms

**Good example**:
> "We hypothesize an inverted-U relationship between internationalization and performance. In early stages, internationalization generates benefits through economies of scale, scope economies, and learning (Contractor et al., 2003), leading to performance gains. However, beyond an optimal point, coordination costs, complexity, and managerial attention limits (Hitt et al., 1997) outweigh these benefits, leading to performance decline (H1)."

---

## Issue Category 2: Construct Definition Problems

### Problem 2.1: Conflating Related but Distinct Constructs

**Description**: Treating different concepts as if they were the same.

**Common conflations**:
- Digitization = Digitalization = Digital Transformation
- Digital capability = Digital adoption
- Institutional distance = Institutional quality = Institutional voids
- Internationalization breadth = Internationalization depth
- Accounting performance = Market performance

**Example**:
> "We measure digital transformation using a binary variable for whether the firm has a website."

**Why it's problematic**:
- Having a website is digitization (basic), not transformation (fundamental business model change)
- Construct validity severely compromised
- Theoretical implications differ dramatically

**How to fix**:
1. Define each construct precisely
2. Cite definitional sources
3. Explain why distinctions matter for your theory
4. Use separate measures for separate constructs

**Good example**:
> "Following Verhoef et al. (2021), we distinguish digital adoption (the breadth of digital tools used, such as website, email, e-commerce) from technological capability (the depth of technology integration, such as foreign technology licensing, R&D activity, quality certification). Digital adoption represents surface-level digitization, while technological capability represents embedded organizational competence. These constructs have different theoretical implications: adoption primarily reduces coordination costs in internationalization (H3), while capability enhances value creation through innovation (H2)."

---

### Problem 2.2: Vague Theoretical Constructs

**Description**: Using fuzzy concepts that could mean many things.

**Example**:
> "We examine the role of 'firm quality' in internationalization."

**Why it's problematic**:
- "Firm quality" could mean: financial health, management quality, product quality, reputation, capabilities, efficiency, or many other things
- Impossible to operationalize clearly
- No theoretical precision

**How to fix**:
1. Replace vague terms with specific theoretical constructs
2. Provide clear definitions
3. Explain what is included and excluded

**Good example**:
> "We examine the role of technological capability, defined as the firm's capacity to develop, adapt, and deploy technology for value creation (Lall, 1992). We operationalize this through three indicators: (1) foreign technology licensing, indicating absorptive capacity; (2) R&D activity, indicating innovation investment; and (3) quality certification, indicating process capability. This construct is distinct from general managerial quality (captured by our control variables) and from digital adoption breadth (H3)."

---

## Issue Category 3: Moderation Logic Problems

### Problem 3.1: Unclear Direction of Moderation

**Description**: Stating that X moderates the Y-Z relationship without specifying how.

**Example**:
> "We hypothesize that digital capability moderates the relationship between internationalization and performance (H2)."

**Why it's problematic**:
- Does digital capability strengthen or weaken the relationship?
- Does it change the slope, the intercept, or the shape?
- At what level of digital capability does the effect occur?

**How to fix**:
1. Specify the direction: "strengthens", "weakens", "attenuates", "amplifies"
2. For curvilinear relationships, specify whether moderator affects the slope, the turning point, or the overall curvature
3. Provide theoretical logic for the specific pattern

**Good example**:
> "We hypothesize that technological capability positively moderates the internationalization-performance relationship, such that the positive slope in the early stage is steeper and the negative slope in the over-internationalization stage is less steep for high-TCI firms. Mechanistically, high-TCI firms extract more value from each unit of internationalization (steeper early gains) and manage complexity better (delayed over-internationalization costs) (H2)."

---

### Problem 3.2: Moderator-Mediator Confusion

**Description**: Proposing moderation when the logic actually implies mediation, or vice versa.

**Moderation**: X affects Y differently depending on level of Z
**Mediation**: X affects Y through Z

**Example of confusion**:
> "We hypothesize that digital capability moderates the internationalization-performance relationship. Specifically, internationalization increases digital capability, which in turn improves performance."

**Why it's problematic**:
- The second sentence describes mediation (I → DC → P), not moderation
- Different statistical tests required
- Different theoretical implications

**How to fix**:
1. Ask: "Does Z change *how* X affects Y (moderation) or does Z carry the effect of X to Y (mediation)?"
2. Draw the conceptual model
3. Ensure hypothesis wording matches the diagram

**Moderation example**:
> "Digital capability moderates the I-P relationship: at high levels of DC, the positive effect of internationalization on performance is stronger (H3a)."

**Mediation example**:
> "Internationalization improves performance partially through the mediating mechanism of digital capability development: international exposure drives digital adoption, which enhances efficiency (H3b)."

---

### Problem 3.3: Too Many Interactions

**Description**: Proposing three-way or four-way interactions without strong theoretical justification.

**Example**:
> "We hypothesize a four-way interaction between internationalization, digital capability, institutional quality, and firm size in predicting performance (H7)."

**Why it's problematic**:
- Four-way interactions are extremely difficult to interpret
- Require very large samples to have statistical power
- Often theoretically unjustified
- Reviewers will be skeptical

**How to fix**:
1. Start with two-way interactions
2. Only propose three-way interactions if there's strong theoretical reason
3. Avoid four-way or higher unless absolutely essential
4. For three-way, clearly explain: "Z moderates the moderating effect of W on the X-Y relationship because..."

**Good example**:
> "We propose a three-way interaction among internationalization, digital adoption, and institutional regime (H5c). Specifically, the positive moderating effect of digital adoption on the I-P relationship (H3) is stronger in institutionally weak regimes (Frontier, SIDS) than in strong regimes (Advanced). This is because digital tools serve as institutional substitutes (Khanna & Palepu, 2010), bypassing weak formal institutions—a benefit that is less relevant where institutions already function well."

---

## Issue Category 4: Boundary Condition Problems

### Problem 4.1: Ignoring Scope Conditions

**Description**: Claiming universal relationships without specifying where they apply.

**Example**:
> "We hypothesize an inverted-U relationship between internationalization and performance."

**Why it's problematic**:
- The inverted-U may not hold for all firm types (e.g., born-globals, platform firms)
- May not hold in all industries (e.g., extractive vs. manufacturing vs. services)
- May not hold in all countries (e.g., SIDS with forced internationalization)

**How to fix**:
1. Specify the scope: "For [type of firms] in [type of industries] from [type of countries]..."
2. Acknowledge boundary conditions
3. If possible, test boundary conditions empirically

**Good example**:
> "We hypothesize an inverted-U relationship between internationalization and performance for manufacturing and services firms in Asian emerging and frontier markets (H1). However, we expect this relationship to break down in Pacific SIDS, where extreme market smallness forces internationalization regardless of firm readiness, leading to a monotonic negative relationship (H1b—boundary condition)."

---

### Problem 4.2: Not Addressing Obvious Counterarguments

**Description**: Ignoring well-known contradictory evidence or theories.

**Example**:
> "Following Uppsala Model, we argue that internationalization is always gradual and sequential."

**Why it's problematic**:
- Born-global literature directly contradicts this
- Reviewers will immediately raise this objection
- Appears unaware of the literature

**How to fix**:
1. Acknowledge counterarguments explicitly
2. Explain why your context or framing differs
3. Position your work as conditional, not universal

**Good example**:
> "The Uppsala Model predicts gradual, sequential internationalization (Johanson & Vahlne, 1977). However, born-global firms and digital platforms challenge this pattern (Stallkamp & Schotter, 2021). We argue that Uppsala logic remains relevant for the learning cost mechanism, even if the speed and sequence have changed in the digital era. Specifically, we retain Uppsala's insight about liability of foreignness and learning-by-doing, but extend it by proposing that digital capabilities enable data-augmented learning (Banalieva & Dhanaraj, 2019), accelerating but not eliminating the learning process."

---

## Issue Category 5: Measurement-Theory Alignment Problems

### Problem 5.1: Measuring the Wrong Thing

**Description**: Operationalization doesn't match the theoretical construct.

**Example**:
> "We theorize about international experience but measure it as number of countries entered."

**Why it's problematic**:
- Number of countries = breadth of internationalization (scope)
- Experience = time × learning (process)
- These are different constructs with different implications

**How to fix**:
1. Ensure measure matches construct definition
2. If perfect measure unavailable, acknowledge limitation
3. Consider multiple indicators (triangulation)

**Good example**:
> "We theorize about internationalization intensity, defined as the extent of firm resources committed to foreign markets (Contractor et al., 2003). We measure this using foreign sales to total sales (FSTS), which captures revenue internationalization. We acknowledge that this does not capture asset or employment internationalization; however, for our sample of manufacturing and services firms, sales intensity is the most appropriate and widely used measure (Sullivan, 1994; Kirca et al., 2012)."

---

### Problem 5.2: Ignoring Endogeneity

**Description**: Not addressing obvious endogeneity concerns in theoretical development.

**Example**:
> "We hypothesize that internationalization improves performance."

**Why it's problematic**:
- Reverse causality: high-performing firms may internationalize more
- Omitted variables: both I and P may be driven by unobserved capabilities
- Reviewers will immediately raise this concern

**How to fix**:
1. Acknowledge endogeneity explicitly in theory section
2. Discuss theoretical logic for causal direction
3. Outline empirical strategy to address it (IV, lagged variables, FE, etc.)

**Good example**:
> "We theorize that internationalization affects performance through learning and scale mechanisms (H1). However, we acknowledge potential reverse causality: high-performing firms may have more resources to internationalize (selection effect). To isolate the causal effect of internationalization on performance, we employ: (1) one-year lagged internationalization measures, (2) firm fixed effects to control for time-invariant unobserved heterogeneity, and (3) dynamic panel GMM in robustness checks. Theoretically, our focus on the *change* in performance following internationalization (rather than level) emphasizes the causal mechanism."

---

## Issue Category 6: Literature Positioning Problems

### Problem 6.1: Claiming Novelty for Non-Novel Ideas

**Description**: Presenting well-established ideas as if they were new.

**Example**:
> "We are the first to propose that internationalization may have costs as well as benefits."

**Why it's problematic**:
- This has been known since at least Hymer (1976) on liability of foreignness
- Extensive literature on internationalization costs
- Damages credibility

**How to fix**:
1. Thoroughly review literature before claiming novelty
2. Position contribution as extension, integration, or contextualization rather than discovery
3. Be specific about what is novel

**Good example**:
> "The costs and benefits of internationalization are well-established (Zaheer, 1995; Lu & Beamish, 2004). Our contribution is threefold: (1) we integrate digital capabilities as a novel moderator that has emerged only in the last decade, (2) we test this in the underexplored Asian context across 47 economies, and (3) we specify institutional regime heterogeneity using a six-regime ICRV framework that captures finer-grained variation than prior binary emerging/developed classifications."

---

### Problem 6.2: Ignoring Contradictory Evidence

**Description**: Citing only studies that support your hypotheses.

**Example**:
> "Prior research consistently shows that internationalization improves performance (cite 5 supporting studies)."

**Why it's problematic**:
- Meta-analyses show mixed findings (Bausch & Krist, 2007; Wu et al., 2022)
- Ignoring contradictory evidence appears selective or uninformed
- Reviewers will point this out

**How to fix**:
1. Acknowledge mixed findings explicitly
2. Explain why findings are mixed (heterogeneity, moderators, context)
3. Position your study as resolving inconsistency

**Good example**:
> "The internationalization-performance relationship remains theoretically debated and empirically inconsistent. Meta-analyses find an overall small positive effect (r=0.10-0.16), but with extremely high heterogeneity (I² > 80%) (Bausch & Krist, 2007; Kirca et al., 2012; Wu et al., 2022). Some studies find positive linear effects (cite), others find inverted-U (cite), and still others find no significant relationship (cite). This heterogeneity suggests that the I-P relationship is highly contingent on firm capabilities, institutional context, and industry characteristics—precisely the moderators we examine in our multi-theory framework."

---

## Issue Category 7: Temporal Logic Problems

### Problem 7.1: Static Theory for Dynamic Phenomenon

**Description**: Treating internationalization as a static state rather than a dynamic process.

**Example**:
> "We examine how level of internationalization affects performance."

**Why it's problematic**:
- Internationalization is a process that unfolds over time
- Effects may differ in short-run vs. long-run
- Learning and adjustment are temporal processes

**How to fix**:
1. Incorporate temporal dimension into theory
2. Distinguish short-term costs from long-term benefits
3. Consider dynamic panel models

**Good example**:
> "We theorize internationalization as a dynamic process with time-varying effects (Johanson & Vahlne, 1977, 2009). In the short run (0-2 years), internationalization incurs learning costs and liability of foreignness (Zaheer, 1995), potentially reducing performance. In the medium run (3-5 years), learning benefits and scale economies emerge, improving performance. In the long run (5+ years), over-internationalization may lead to coordination costs exceeding benefits (Contractor et al., 2003). Our empirical strategy uses lagged internationalization measures to capture the medium-run effects, and we test temporal heterogeneity in H6 using two-wave data from China."

---

### Problem 7.2: Ignoring Feedback Loops

**Description**: Assuming one-way causality when bidirectional relationships exist.

**Example**:
> "Internationalization → Performance (H1)"

**Why it's problematic**:
- Performance may enable further internationalization (feedback)
- Digital capabilities may be both cause and consequence of internationalization
- Ignoring feedback leads to biased estimates

**How to fix**:
1. Acknowledge feedback in theory section
2. Discuss implications for identification
3. Use appropriate methods (e.g., instrumental variables, dynamic panel GMM)

**Good example**:
> "We theorize that internationalization affects performance (H1), but acknowledge potential feedback: successful internationalization generates resources that enable further international expansion, creating a virtuous cycle. Similarly, internationalization may drive digital capability development, which we model as a moderator (H3). To address simultaneity, we: (1) use lagged internationalization in baseline models, (2) include firm fixed effects to absorb time-invariant confounders, and (3) employ system GMM in robustness tests to explicitly model the dynamic feedback process."

---

## Issue Category 8: Cross-Level Inference Problems

### Problem 8.1: Ecological Fallacy

**Description**: Inferring firm-level relationships from country-level patterns.

**Example**:
> "Countries with higher digitalization have better economic performance; therefore, firms with higher digitalization will have better internationalization performance."

**Why it's problematic**:
- Country-level and firm-level mechanisms may differ
- Composition effects, aggregation bias
- Classic ecological fallacy

**How to fix**:
1. Match level of theory to level of inference
2. If using multi-level data, use multi-level theory and methods
3. Be explicit about cross-level mechanisms

**Good example**:
> "We theorize at the firm level: digital adoption (firm-level construct) moderates the firm-level I-P relationship. However, we also recognize that country-level institutional context (ICRV regime) creates different environments for this firm-level relationship. This is a cross-level interaction: country-level institutions moderate the firm-level digital adoption effect (H5). We test this using multilevel modeling with random slopes, allowing the firm-level digital adoption coefficient to vary by ICRV regime."

---

### Problem 8.2: Aggregation Without Justification

**Description**: Aggregating lower-level data to higher level without theoretical reason.

**Example**:
> "We aggregate firm-level internationalization data to industry-level and test industry-level performance effects."

**Why it's problematic**:
- Loses firm-level variation (information loss)
- Aggregation may create spurious relationships
- Need strong theoretical reason for aggregation

**How to fix**:
1. Only aggregate if theory operates at the aggregated level
2. Explain the theoretical mechanism at the aggregated level
3. Consider multi-level modeling as alternative

**Good example**:
> "We analyze firm-level data because our theory concerns firm-level capabilities and firm-level performance outcomes. While we control for industry effects (industry fixed effects), we do not aggregate to industry level because our theoretical mechanisms (learning, capability deployment, institutional navigation) operate at the firm level. However, we do allow for industry-level heterogeneity by testing our hypotheses separately for manufacturing vs. services sectors in robustness checks."

---

## Checklist: Avoiding Common Theoretical Issues

Before submitting your theoretical framework chapter:

### Theory Integration
- [ ] I have 2-4 core theories (not 5+)
- [ ] I explain the specific role of each theory
- [ ] I show how theories complement each other
- [ ] Each hypothesis maps clearly to a theory

### Constructs
- [ ] All key constructs are precisely defined
- [ ] I distinguish between related but different constructs
- [ ] Definitions are cited from literature
- [ ] Operationalizations match definitions

### Hypotheses
- [ ] Each hypothesis has explicit theoretical derivation
- [ ] Causal mechanisms are specified (not just relationships)
- [ ] Direction of effects is clear (positive/negative/curvilinear)
- [ ] For moderators: I specify *how* they moderate (strengthen/weaken/change shape)

### Mechanisms
- [ ] I explain *why* and *how*, not just *what*
- [ ] Mediating processes are identified
- [ ] I distinguish my mechanism from alternatives
- [ ] Temporal sequence is clear

### Moderation Logic
- [ ] I distinguish moderation from mediation
- [ ] Direction of moderation is specified
- [ ] I avoid three-way+ interactions unless essential
- [ ] For curvilinear relationships: I specify whether moderator affects slope, turning point, or shape

### Boundary Conditions
- [ ] I specify scope conditions (what firms, industries, countries)
- [ ] I acknowledge boundary conditions where theory breaks down
- [ ] I address obvious counterarguments
- [ ] I position my work as conditional, not universal

### Literature Positioning
- [ ] I acknowledge mixed prior findings
- [ ] I cite contradictory evidence, not just supporting evidence
- [ ] I am specific about my novel contribution
- [ ] I don't claim novelty for established ideas

### Measurement-Theory Alignment
- [ ] Measures match constructs
- [ ] I acknowledge endogeneity concerns
- [ ] I outline empirical strategy to address endogeneity
- [ ] I discuss construct validity

### Temporal Logic
- [ ] I treat internationalization as a process, not just a state
- [ ] I distinguish short-run vs. long-run effects
- [ ] I acknowledge feedback loops
- [ ] I use appropriate temporal lags

### Cross-Level Logic
- [ ] Level of theory matches level of analysis
- [ ] Cross-level mechanisms are explicit
- [ ] I avoid ecological fallacy
- [ ] Aggregation (if any) is justified

---

## When to Seek Help

Consult your advisor or a methods expert if:

1. You're unsure whether your logic implies moderation or mediation
2. You're proposing three-way or higher interactions
3. You have obvious endogeneity but don't know how to address it
4. Your theories seem to contradict each other
5. You can't clearly explain the causal mechanism
6. Your hypotheses don't seem testable with your data
7. You're getting contradictory feedback from different readers

Early consultation prevents major revisions later.

---

**Remember**: Most theoretical problems are fixable. The key is to identify them early, before you've collected data or run analyses. A strong theoretical foundation makes everything else easier.