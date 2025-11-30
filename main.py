from graph.define_graph import build_graph
from datetime import datetime
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="language 공부하기")
    parser.add_argument("--url", type=str, required=True)
    parser.add_argument("--title", type=str, default="오늘도 화이팅")
    parser.add_argument("--date", type=str, default=None)

    args = parser.parse_args()
    date_str = args.date if args.date else datetime.now().strftime("%Y-%m-%d")

    app = build_graph()
    result = app.invoke({
        "url": args.url,
        "title_text": args.title,
        "date_str": date_str
    })