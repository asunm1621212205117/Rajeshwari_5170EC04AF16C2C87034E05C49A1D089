def LinearSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
    if product==tragetProduct:
      indices.append(index)

return indices
products=["shoes","boots","loafer","shoes","sandals","shoes"]
target="shoes"
target="apple"
result=LinearSearchProduct(products,target)
print(result)