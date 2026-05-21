# CodeReview Findings

- Source: `r.py`
- Generated: `2026-05-21T07:32:26.949Z`
- Findings: **1**

> Click the CodeLens buttons (Apply Fix / Generate Fix / Reject) shown above each finding.

---

<!-- codereview:actions docUri="file:///c%3A/Users/shrav/Downloads/Admin%20website/r.py" idx=0 sidecarUri="file:///c%3A/Users/shrav/Downloads/Admin%20website/.codereview/r.py.findings.json" hasFix=false source="r.py" -->
## 1. Logic Bug
- Type: `security`
- Severity: `low`
- Location: `c:\Users\shrav\Downloads\Admin website\r.py:10`

**Problem**

Division by zero in average calculation.

**Current code (lines 10-13)**

```python
     9 | numbers = [10, 20, 30]
>   10 | 
>   11 | print("First number is " + numbers[0])
>   12 | 
>   13 | average = sum(numbers) / 0
    14 | # CodeReview: removed potentially sensitive print()
```

**Expected code**

_No fix generated yet. Click_ `Generate Fix` _above to request one._

Actions: [Apply Fix (will generate)](command:codereview.applyFixFromReport?%5B%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fshrav%2FDownloads%2FAdmin%2520website%2Fr.py%22%2C0%2C%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fshrav%2FDownloads%2FAdmin%2520website%2F.codereview%2Fr.py.findings.json%22%5D) · [Generate Fix](command:codereview.generateFixFromReport?%5B%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fshrav%2FDownloads%2FAdmin%2520website%2Fr.py%22%2C0%2C%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fshrav%2FDownloads%2FAdmin%2520website%2F.codereview%2Fr.py.findings.json%22%5D) · [Reject](command:codereview.rejectFindingFromReport?%5B%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fshrav%2FDownloads%2FAdmin%2520website%2Fr.py%22%2C0%2C%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fshrav%2FDownloads%2FAdmin%2520website%2F.codereview%2Fr.py.findings.json%22%5D)
