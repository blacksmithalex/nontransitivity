results = pivot_table(dfs)
d = {'2017': results[0], '2018': results[1], '2019': results[2], '2020': results[3], '2021':results[4]}
out = pd.DataFrame(d, index=['s1 > s2', 's1 > s3', 's2 > s1','s2 > s3', 's3 > s1', 's3 > s2','s1 == s2', 's1 == s3', 's2 == s3', 'Num of days'])
out