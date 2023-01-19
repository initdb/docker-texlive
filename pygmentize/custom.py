from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, \
        Error, Generic, Number, Operator, Whitespace


class CustomStyle(Style):
     background_color = "#ececec"

     styles = {
          Whitespace:                "#bbbbbb",
          Comment:                   "italic #3D7B7B",
          Comment.Preproc:           "noitalic #9C6500",

          Keyword:                   "bold #00809f",
          Keyword.Pseudo:            "nobold",
          Keyword.Type:              "nobold #B00040",

          Operator:                  "#666666",
          Operator.Word:             "bold #AA22FF",

          Name.Builtin:              "#00809f",
          Name.Function:             "#00809f",
          Name.Class:                "bold #00809f",
          Name.Namespace:            "bold #00809f",
          Name.Exception:            "bold #CB3F38",
          Name.Variable:             "#19177C",
          Name.Constant:             "#880000",
          Name.Label:                "#767600",
          Name.Entity:               "bold #717171",
          Name.Attribute:            "#687822",
          Name.Tag:                  "bold #00809f",
          Name.Decorator:            "#AA22FF",

          String:                    "#007771",
          String.Doc:                "italic",
          String.Interpol:           "bold #A45A77",
          String.Escape:             "bold #AA5D1F",
          String.Regex:              "#A45A77",
          String.Symbol:             "#19177C",
          String.Other:              "#00809f",
          Number:                    "#666666",

          Generic.Heading:           "bold #000080",
          Generic.Subheading:        "bold #003e76",
          Generic.Deleted:           "#A00000",
          Generic.Inserted:          "#008400",
          Generic.Error:             "#E40000",
          Generic.Emph:              "italic",
          Generic.Strong:            "bold",
          Generic.Prompt:            "bold #000080",
          Generic.Output:            "#717171",
          Generic.Traceback:         "#04D",

          Error:                     "border:#FF0000"
          }
