def pivot_table(dfs, a = 0.3, b = 0.6):
    results = []
    for df in dfs:
        days = sorted(list(set(df['<DATE>'])))
        s1income = [0] * len(days)
        s2income = []
        s3income = []
        for d in days:
            s2income.append(strategy23(df,d, a, b))
            s3income.append(strategy23(df,d, b, a))
        s1betters2 = betterthan(s1income, s2income)
        s1betters3 = betterthan(s1income, s3income)
        s2betters1 = betterthan(s2income, s1income)
        s2betters3 = betterthan(s2income, s3income)
        s3betters1 = betterthan(s3income, s1income)
        s3betters2 = betterthan(s3income, s2income)
        s1isequals2 = len(days) - s1betters2 - s2betters1
        s1isequals3 = len(days) - s1betters3 - s3betters1
        s2isequals3 = len(days) - s2betters3 - s3betters2
        results.append(['paste all *betters* here'])
    return results  