class Solution:
    def maxProduct(self, prefix_product: List[int]) -> int:
        """
        배열에 0 인 요소가 없다면 가장 큰 곱의 부분배열은 첫 요소 또는 마지막 요소 부터 시작한다
        그렇기에 prefix, suffix 를 미리 계산한 배열의 최댓값이 답이 된다.
        만약 배열에 0 인 요소가 있다면 0을 중심으로 여러개의 부분배열로 나누어 계산한다
        """
        suffix_product = prefix_product[::-1]
        for i in range(1, len(prefix_product)):
            prefix_product[i] *= prefix_product[i - 1] or 1
            suffix_product[i] *= suffix_product[i - 1] or 1
        return max(prefix_product+suffix_product)