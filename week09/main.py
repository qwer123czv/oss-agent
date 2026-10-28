import tools
#print(tools.get_boxoffice_rank_1("20260824"))

count = tools.get_movie_audience("20260824", "오디세이")
print(f"->{count:,}명")
count = tools.get_movie_audience("20260824", "호프")
print(f"->{count:,}명")
count = tools.get_movie_audience("20260824", "없는영화")
print(f"->{count}")
