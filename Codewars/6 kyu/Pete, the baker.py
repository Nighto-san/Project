def cakes(recipe, available):
    res = []
    for i in recipe:
        try:
            res.append(available[i]//recipe[i])
        except KeyError:
            return 0
    return min(res)










print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flwour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))