def build_chart(results):

    if not results:
        return {}


    first_row = results[0]


    keys = list(first_row.keys())


    if len(keys) >= 2:

        return {

            "type": "bar",

            "x": keys[0],

            "y": keys[1]

        }


    return {}