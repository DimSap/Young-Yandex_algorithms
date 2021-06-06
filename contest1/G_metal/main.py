N, K, M = list(map(int, input().split()))
if N < K or K < M:
    print(0)
else:
    sum_details = 0
    det_from_one_sample = K//M
    kg_from_one_sample_left = K - det_from_one_sample * M
    while N >= K:
        n_samples = N//K
        kg_samples_left = N - K*n_samples
        kg_details_left = kg_from_one_sample_left * n_samples

        sum_details += n_samples * det_from_one_sample
        N = kg_details_left + kg_samples_left
    print(sum_details)