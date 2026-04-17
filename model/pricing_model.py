def get_dynamic_price(demand, base_price, month=None):

    demand = float(demand)
    demand = max(0, min(10, demand))

    # 🔥 SAME ADJUSTMENT (aligned with demand logic)
    adjusted = demand - (base_price / 100)
    adjusted = adjusted * 1.3   # scaling boost

    # 🔥 SEASON FACTOR
    season_factor = 1
    if month in [11, 12]:   # festive
        season_factor = 1.05
    elif month in [6, 7]:   # off-season
        season_factor = 0.97

    # 🔥 CORRECTED PRICING RULES

    # HIGH DEMAND (≥ 6)
    if adjusted >= 6:
        price = base_price * 1.15

    # MODERATE DEMAND (3–6)
    elif adjusted >= 3:
        price = base_price * 1.05

    # LOW DEMAND (< 3)
    else:
        price = base_price * 0.9

    return price * season_factor
