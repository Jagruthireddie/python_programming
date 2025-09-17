t = [("yashu", 90), ("jagu", 80), ("deek", 50), ("akh", 66), ("srija", 55)]
l = 0
p = ""
for n, s in t:
    if s > l:
        l = s
        p = n
    if s>75:
        print("Student name",n,"score",s)
print("Highest scorer:", p, "with score", l)
