ann = MLP(2, 10, 1)
%timeit -n 1 -r 1 ann.train(zip(X,y), iterations=100)
plot_decision_boundary(ann)
plt.title("Modelo con 10 unidades ocultas y 100 iteraciones")
