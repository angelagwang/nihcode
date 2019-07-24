import pandas as pd

data = pd.read_csv("Code6Tweets.csv", dtype = "unicode")
df = data[data['user.location'].notnull()]

def tweetCount(input):
    statedict = {"AL":0, "AK":0, "AZ":0, "AR":0, "CA":0, "CO":0, "CT":0, "DC":0, "DE":0, "FL":0, "GA":0, "HI":0, "ID":0, "IL":0,"IN":0,"IA":0,"KS":0,"KY":0,"LA":0,"ME":0, "MD":0,"MA":0,"MI":0,"MN":0,"MS":0,"MO":0,"MT":0,"NE":0,"NV":0,"NH":0,"NJ":0,"NM":0,"NY":0,"NC":0,"ND":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"WV":0,"WI":0,"WY":0}
    for item in input:
        if "Alabama" in item or "AL" in item:
            statedict["AL"] = statedict["AL"] + 1
        elif "Arkansas" in item or "AK" in item:
            statedict["AK"] = statedict["AK"] + 1
        elif "Arizona" in item or "AZ" in item:
            statedict["AZ"] = statedict["AZ"] + 1
        elif "Arkansas" in item or "AR" in item:
            statedict["AR"] = statedict["AR"] + 1
        elif "California" in item or "CA" in item:
            statedict["CA"] = statedict["CA"] + 1
        elif "Colorado" in item or "CO" in item:
            statedict["CO"] = statedict["CO"] + 1
        elif "Conneticut" in item or "CT" in item:
            statedict["CT"] = statedict["CT"] + 1
        elif "District of Columbia" in item or "DC" in item:
            statedict["DC"] = statedict["DC"] + 1
        elif "Deleware" in item or "DE" in item:
            statedict["DE"] = statedict["DE"] + 1
        elif "Florida" in item or "FL" in item:
            statedict["FL"] = statedict["FL"] + 1
        elif "Georgia" in item or "GA" in item:
            statedict["GA"] = statedict["GA"] + 1
        elif "Hawaii" in item or "HI" in item:
            statedict["HI"] = statedict["HI"] + 1
        elif "Idaho" in item or "ID" in item:
            statedict["ID"] = statedict["ID"] + 1
        elif "Illinois" in item or "IL" in item:
            statedict["IL"] = statedict["IL"] + 1
        elif "Indiana" in item or "IN" in item:
            statedict["IN"] = statedict["IN"] + 1
        elif "Iowa" in item or "IA" in item:
            statedict["IA"] = statedict["IA"] + 1
        elif "Kansas" in item or "KS" in item:
            statedict["KS"] = statedict["KS"] + 1
        elif "Kentucky" in item or "KY" in item:
            statedict["KY"] = statedict["KY"] + 1
        elif "Louisiana" in item or "LA" in item:
            statedict["LA"] = statedict["LA"] + 1
        elif "Maine" in item or "ME" in item:
            statedict["ME"] = statedict["ME"] + 1
        elif "Maryland" in item or "MD" in item:
            statedict["MD"] = statedict["MD"] + 1
        elif "Massachusetts" in item or "MA" in item:
            statedict["MA"] = statedict["MA"] + 1
        elif "Michigan" in item or "MI" in item:
            statedict["MI"] = statedict["MI"] + 1
        elif "Minnesota" in item or "MN" in item:
            statedict["MN"] = statedict["MN"] + 1
        elif "Mississippi" in item or "MS" in item:
            statedict["MS"] = statedict["MS"] + 1
        elif "Missouri" in item or "MO" in item:
            statedict["MO"] = statedict["MO"] + 1
        elif "Montana" in item or "MT" in item:
            statedict["MT"] = statedict["MT"] + 1
        elif "Nebraska" in item or "NE" in item:
            statedict["NE"] = statedict["NE"] + 1
        elif "Nevada" in item or "NV" in item:
            statedict["NV"] = statedict["NV"] + 1
        elif "New Hampshire" in item or "NH" in item:
            statedict["NH"] = statedict["NH"] + 1
        elif "New Jersey" in item or "NJ" in item:
            statedict["NJ"] = statedict["NJ"] + 1
        elif "New Mexico" in item or "NM" in item:
            statedict["NM"] = statedict["NM"] + 1
        elif "New York" in item or "NY" in item:
            statedict["NY"] = statedict["NY"] + 1
        elif "North Carolina" in item or "NC" in item:
            statedict["NC"] = statedict["NC"] + 1
        elif "North Dakota" in item or "ND" in item:
            statedict["ND"] = statedict["ND"] + 1
        elif "Ohio" in item or "OH" in item:
            statedict["OH"] = statedict["OH"] + 1
        elif "Oklahoma" in item or "OK" in item:
            statedict["OK"] = statedict["OK"] + 1
        elif "Oregon" in item or "OR" in item:
            statedict["OR"] = statedict["OR"] + 1
        elif "Pennsylvania" in item or "PA" in item:
            statedict["PA"] = statedict["PA"] + 1
        elif "Rhode Island" in item or "RI" in item:
            statedict["RI"] = statedict["RI"] + 1
        elif "South Carolina" in item or "SC" in item:
            statedict["SC"] = statedict["SC"] + 1
        elif "South Dakota" in item or "SD" in item:
            statedict["SD"] = statedict["SD"] + 1
        elif "Tennessee" in item or "TN" in item:
            statedict["TN"] = statedict["TN"] + 1
        elif "Texas" in item or "TX" in item:
            statedict["TX"] = statedict["TX"] + 1
        elif "Utah" in item or "UT" in item:
            statedict["UT"] = statedict["UT"] + 1
        elif "Vermont" in item or "VT" in item:
            statedict["VT"] = statedict["VT"] + 1
        elif "Virginia" in item or "VA" in item:
            statedict["VA"] = statedict["VA"] + 1
        elif "Washington" in item or "WA" in item:
            statedict["WA"] = statedict["WA"] + 1
        elif "West Virginia" in item or "WV" in item:
            statedict["WV"] = statedict["WV"] + 1
        elif "Wisconsin" in item or "WI" in item:
            statedict["WI"] = statedict["WI"] + 1
        elif "Wyoming" in item or "WY" in item:
            statedict["WY"] = statedict["WY"] + 1
       
    return statedict

print(tweetCount(df["user.location"]))



