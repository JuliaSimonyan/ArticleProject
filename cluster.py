import ast
import timeit
import numpy as np
from sklearn.cluster import KMeans
import inspect

def extract_features(func):
    source_code = inspect.getsource(func)
    code_ast = ast.parse(source_code)

    complexity = sum(isinstance(node, (ast.For, ast.While, ast.If)) for node in ast.walk(code_ast))
    num_func_calls = sum(isinstance(node, ast.Call) for node in ast.walk(code_ast))

    # Check if the function is 'factorial' to handle it differently
    if func.__name__ == 'factorial':
        exec_time = timeit.timeit(lambda: func(5), number=1000)  # Pass a single integer
    else:
        exec_time = timeit.timeit(lambda: func([64, 34, 25, 12, 22, 11, 90]), number=1000)

    return {
        'complexity': complexity,
        'num_func_calls': num_func_calls,
        'exec_time': exec_time
    }

def cluster_snippets(snippets):
    features = np.array([[
        extract_features(snippet)['complexity'],
        extract_features(snippet)['num_func_calls'],
        extract_features(snippet)['exec_time']
    ] for snippet in snippets])

    kmeans = KMeans(n_clusters=2, random_state=0)
    clusters = kmeans.fit_predict(features)
    return clusters
