from flask import Flask
import random
import math


app = Flask(__name__)

CIRCLE_RADIUS = 20
DURATION = 0.3
MARGIN = 40
CANVAS_MAX = 1000
CANVAS_CENTER = CANVAS_MAX / 2
HTML_CONTAINER = """
<html>
<script>
function saynumber() {{
  var msg = new SpeechSynthesisUtterance("{}");
  var list = document.getElementsByClassName("dot");
  for (var i = 0; i < list.length; i++) {{ list[i].style.display = "block"; }}
  window.speechSynthesis.speak(msg);
  msg.onend = function (event) {{ setTimeout(function(){{ location.reload(); }}, 1000); }}
}}
</script>
<body>
{}
</body>
</html>
"""
SVG_CONTAINER = """
<svg id="dots" viewBox="0 0 {} {}" height="100%" width="100%" onclick="saynumber();" xmlns="http://www.w3.org/2000/svg">
{}
</svg>
""".format(
    CANVAS_MAX, CANVAS_MAX, "{}"
)

CIRCLE_CONTAINER = """
<circle class="dot" style="display:none" cx="{}" cy="{}" r="{}">
  	    <animate attributeType="XML"
             attributeName="r"
             from="0" to="{}" dur="{}s"
             fill="freeze" />
</circle>
""".format(
    "{}", "{}", CIRCLE_RADIUS, CIRCLE_RADIUS, DURATION
)


def distance_between_points(a, b):
    x_dist = a[0] - b[0]
    y_dist = a[1] - b[1]
    return math.sqrt((x_dist ** 2) + (y_dist ** 2))


def overlaps(a, b):
    return distance_between_points(a, b) < (CIRCLE_RADIUS + MARGIN)


def overlaps_any(proposed_dot, dots):
    for dot in dots:
        if overlaps(dot, proposed_dot):
            return True
    return False


def outside_range(dot):
    return (
        max(abs(dot[0] - CANVAS_CENTER), abs(dot[1] - CANVAS_CENTER))
        > CANVAS_CENTER - MARGIN
    )


def generate_dots(dots_wanted):
    dots = []
    while len(dots) < dots_wanted:
        proposed_dot = [
            random.normalvariate(0, 1)
            * math.log(len(dots) + 1, 20)
            * 2
            * (CIRCLE_RADIUS + MARGIN)
            + CANVAS_CENTER
            for i in range(2)
        ]
        if overlaps_any(proposed_dot, dots) or outside_range(proposed_dot):
            continue
        else:
            dots.append(proposed_dot)
    return dots


@app.route("/<int:min_dots>/<int:max_dots>")
def home(min_dots, max_dots):
    num_dots = random.randint(min_dots, max_dots)
    circles = generate_dots(num_dots)
    circle_string = "".join([CIRCLE_CONTAINER.format(*circle) for circle in circles])
    inner_html = SVG_CONTAINER.format(circle_string)
    return HTML_CONTAINER.format(num_dots, inner_html)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
