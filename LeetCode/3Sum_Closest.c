#include <stdlib.h>

static int cmp (const void *p, const void *q)
{
    return *(int*)p < *(int*)q ? -1 : 1;
}

int threeSumClosest (int *a, const int n, const int target)
{
    qsort(a, n, sizeof *a, cmp);
    int closest = a[0] + a[1] + a[2];
    for (int i = 0; i < n; ++i) {
        int l = i + 1;
        int r = n - 1;
        while (l < r) {
            const int sum = a[i] + a[l] + a[r];
            if (sum < target)
                ++l;
            else if (sum > target)
                --r;
            else // sum == target
                return target;
            if (abs(sum - target) < abs(closest - target))
                closest = sum;
        }
    }
    return closest;
}
