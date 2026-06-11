# Stata Commands Quick Reference

## File Operations

### Loading Data
```stata
use filename.dta [, clear]           // Load Stata dataset
use varlist using filename [, clear] // Load specific variables
use if condition using filename      // Load with condition
sysuse filename                      // Load system dataset
```

### Saving Data
```stata
save filename [, replace]            // Save current dataset
saveold filename [, replace version(#)] // Save in older format
export delimited using file.csv      // Export to CSV
export excel using file.xlsx         // Export to Excel
```

### Importing Data
```stata
import delimited file.csv, clear     // Import CSV
import excel file.xlsx, firstrow clear // Import Excel
import dbase file.dbf, clear         // Import dBase
```

## Data Exploration

```stata
describe                             // Dataset structure
summarize [varlist]                  // Summary statistics
summarize var, detail                // Detailed statistics
tabulate var1 [var2]                 // Frequency tables
list [varlist] in 1/10               // List first 10 observations
codebook varlist                     // Detailed variable info
inspect varlist                      // Data quality check
```

## Data Manipulation

### Generating Variables
```stata
generate newvar = expression         // Create new variable
replace var = expression if condition // Modify existing variable
egen newvar = function(var)          // Extended generate
recode var (old=new) (old=new)       // Recode values
```

### Dropping and Keeping
```stata
drop varlist                         // Drop variables
keep varlist                         // Keep only these variables
drop if condition                    // Drop observations
keep if condition                    // Keep observations
```

### Sorting and Ordering
```stata
sort varlist                         // Sort data
gsort -var1 +var2                    // Sort descending/ascending
order var1 var2                      // Reorder variables
```

## Statistical Analysis

### Descriptive Statistics
```stata
tabstat varlist, statistics(mean sd) by(groupvar)
table var1 var2, contents(mean var3)
bysort group: summarize var
```

### Regression Analysis
```stata
regress depvar indepvars             // OLS regression
logit depvar indepvars               // Logistic regression
probit depvar indepvars              // Probit regression
ivregress 2sls depvar (endogvar = instruments) exogvars // IV regression
xtreg depvar indepvars, fe           // Fixed effects panel
```

### Hypothesis Testing
```stata
ttest var1 == var2                   // Paired t-test
ttest var, by(group)                 // Two-sample t-test
test coef1 = coef2                   // Test coefficients
```

## Programming Constructs

### Loops
```stata
foreach var in varlist {
    commands
}

forvalues i = 1/10 {
    commands
}

while condition {
    commands
}
```

### Conditionals
```stata
if condition {
    commands
}
else {
    commands
}
```

### Macros
```stata
local macroname "value"              // Local macro
global macroname "value"             // Global macro
display "`macroname'"                // Use local macro
display "${macroname}"               // Use global macro
```

## Batch Mode Commands

### Unix/Linux/Mac
```bash
stata -b do filename.do              # Batch mode, ASCII log
stata -s do filename.do              # Batch mode, SMCL log
stata < filename.do > output.log &   # Redirect I/O
nohup stata -b do filename.do &      # Run in background
```

### Windows
```cmd
StataMP /b do filename.do            REM Batch, click to exit
StataMP /e do filename.do            REM Batch, auto exit
```

## Log Files

```stata
log using filename.log [, replace]   // Start ASCII log
log using filename.smcl [, replace]  // Start SMCL log
log close                            // Close current log
log close _all                       // Close all logs
capture log close                    // Close if open
```

## Common Options

- `, clear` - Replace data in memory
- `, replace` - Overwrite existing file
- `if condition` - Conditional execution
- `in range` - Observation range (e.g., `in 1/100`)
- `, by(varname)` - By-group processing
- `, detail` - Detailed output

## Error Handling

```stata
capture command                      // Suppress errors
if _rc != 0 {                        // Check return code
    display "Error occurred"
}

assert condition                     // Halt if false
```

## System Information

```stata
display c(current_date)              // Current date
display c(current_time)              // Current time
display c(version)                   // Stata version
display c(processors)                // Number of processors
display c(memory)                    // Available memory
```
