Example Yaml:

"'9110_au_location-14' As gallery.'BrowseLayout_Vertical_TwoTextOneImageVariant_ver4.0'":
    BorderColor: =RGBA(0, 0, 0)
    BorderStyle: =BorderStyle.Dotted
    DisabledBorderColor: ='9110_au_location-14'.BorderColor

There is an input.csv and an output.csv

1. if in an input csv it is written
9110_au_location-14, BorderColor

The output CSV would then be:
9110_au_location-14, BorderColor, =RGBA(0, 0, 0, 0)

2. if the input CSV would look like this:
9110_au_location-14, BorderColor, =RGBA(1, 1, 1, 1).
Then in the yaml =RGBA(0, 0, 0, 0) would be replaced by RGBA(1, 1, 1, 1).

3. if the input CSV looks like this:
9110_au_location-14, DisplayMode, =If(varItem=10, DisplayMode.Edit, DisplayMode.View).

Then the yaml would look like this:
"'9110_au_location-14' As gallery.'BrowseLayout_Vertical_TwoTextOneImageVariant_ver4.0'":
    BorderColor: =RGBA(0, 0, 0)
    BorderStyle: =BorderStyle.Dotted
    DisabledBorderColor: ='9110_au_location-14'.BorderColor
    DisplayMode: =If(varItem=10, DisplayMode.Edit, DisplayMode.View)
