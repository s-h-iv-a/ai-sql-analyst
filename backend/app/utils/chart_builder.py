import pandas as pd
import plotly.express as px


def build_chart(results: list[dict]) -> dict | None:
    if not results:
        return None

    df = pd.DataFrame(results)
    if df.empty or len(df.columns) < 2:
        return None

    x_col = df.columns[0]
    y_candidates = [col for col in df.columns[1:] if pd.api.types.is_numeric_dtype(df[col])]
    if not y_candidates:
        return None

    y_col = y_candidates[0]
    fig = px.bar(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
    return fig.to_dict()
