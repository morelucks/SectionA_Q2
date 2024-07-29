from django.shortcuts import render
from django.http import HttpResponse

def twoSum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

def index(request):
    return render(request, 'twoSumApp/index.html')

def result(request):
    if request.method == 'POST':
        nums = list(map(int, request.POST['nums'].split(',')))
        target = int(request.POST['target'])
        indices = twoSum(nums, target)
        return render(request, 'twoSumApp/results.html', {'indices': indices})
    else:
        return HttpResponse("Invalid request.")
