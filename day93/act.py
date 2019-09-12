package = [
    {"name":"大刀","act":2},
    {"name":"黄金甲","act":5},
    {"name":"屠龙刀","act":15},
    {"name":"绿玉屠龙","act":999}
]
equi=[]

for eq in package:
    if eq.get("name") == "绿玉屠龙":
        # $pull : {"name":"绿玉屠龙","act":999} = eq



