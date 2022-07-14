def generate_view(
    posts: list,
    button_url: str,
    label: str = "This is my page",
    default_text="Type something",
):
    if posts:
        final_data = f"""
            <ul>
                <li>{'</li><li>'.join(posts)}</li>
            </ul>
        """
    else:
        final_data = ""
    base = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog</title>
    </head>

    <body>
        <h1>{label}</h1>
        <form action="{button_url}" method="post">
            <textarea id="post" name="post" rows="5" cols="33">{default_text}</textarea>
            <input type="submit" value="Send Request">
            {final_data}
        </form>
    </body>

    </html>
    """

    return base
