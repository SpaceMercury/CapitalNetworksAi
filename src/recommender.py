import implicit as ipl

model = ipl.als.AlternatingLeastSquares(factors=50, regularization=0.01, iterations=50)

recommendations = model.recommend()

related = models.similar_items(itemid)
