from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, \
        Error, Generic, Number, Operator, Whitespace


class CustomStyle(Style):
     background_color = "#ececec"
     #highlight_color = "#44475a"
     #line_number_color = "#f1fa8c"
     line_number_background_color = "#ececec"
     #line_number_special_color = "#50fa7b"
     line_number_special_background_color = "#ececec"

     styles = {
          Whitespace:                "#bbbbbb",
          Comment:                   "italic #003e76",
          Comment.Preproc:           "noitalic #003e76",

          Keyword:                   "bold #ff9933",
          Keyword.Pseudo:            "nobold",
          Keyword.Type:              "nobold #B00040",

          Operator:                  "#666666",
          Operator.Word:             "bold #AA22FF",

          Name.Builtin:              "#ff9933",
          Name.Function:             "#009DEC",
          Name.Class:                "bold #009DEC",
          Name.Namespace:            "bold #009DEC",
          Name.Exception:            "bold #CB3F38",
          Name.Variable:             "#19177C",
          Name.Constant:             "#880000",
          Name.Label:                "#767600",
          Name.Entity:               "bold #717171",
          Name.Attribute:            "#687822",
          Name.Tag:                  "bold #ff9933",
          Name.Decorator:            "#AA22FF",

          String:                    "#005551",
          String.Doc:                "italic",
          String.Interpol:           "bold #A45A77",
          String.Escape:             "bold #AA5D1F",
          String.Regex:              "#A45A77",
          String.Symbol:             "#19177C",
          String.Other:              "#ff9933",
          Number:                    "#666666",

          Generic.Heading:           "bold #000080",
          Generic.Subheading:        "bold #00809f",
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
