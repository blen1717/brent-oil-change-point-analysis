import pymc as pm
import arviz as az
import numpy as np
import ruptures as rpt

def build_model(data, n_points):
    with pm.Model() as model:
        tau = pm.DiscreteUniform('tau', lower=0, upper=n_points-1)
        mu1 = pm.Normal('mu1', mu=0, sigma=1.0)
        mu2 = pm.Normal('mu2', mu=0, sigma=1.0)
        sigma = pm.HalfNormal('sigma', sigma=0.5)
        idx = np.arange(n_points)
        mu = pm.math.switch(tau >= idx, mu1, mu2)
        obs = pm.Normal('obs', mu=mu, sigma=sigma, observed=data)
    return model

def detect_multiple_change_points(data, pen=10):
    data_reshaped = data.reshape(-1, 1)
    algo = rpt.Pelt(model="rbf").fit(data_reshaped)
    return algo.predict(pen=pen)
  
