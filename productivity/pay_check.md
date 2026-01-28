# Rationale

In the gig economy, people often find themselves with very different take-homes compared to their advertised rate. Weird incentives, early submission bonuses, late penalties and so on can make it tough to figure out exactly what the take-home is (even before tax and platform fees).

'pay_check.py' is a simple linear regression tool for calculating pre-tax hourly rates from pay received and minutes worked. It is based on a null hypothesis that assumes linear scaling across the stated rate. It takes a CSV input with:

```
Duration,Rate,Payable,Type
27m 50s,$47.00/hr,$25.52,Task
1m 16s,$55.00/hr,$1.16,Task
4s,$17.80/hr,$0.02,Bonus
45m 0s,$55.00/hr,$41.25,Task
```

But, of course, this can be customisable for different gigs. It does work best with 20+ inputs and at least a few short-time options to check for performance on very short scales.
