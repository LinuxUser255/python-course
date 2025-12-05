
films = {
    # key : value
    # year: title
    2018: "Black Panther",
    2019: "Avengers: Endgame",
    2020: "Bad Boys for Life"
}

# .keys() gives us the keys
for year in films.keys():
    print(year)
    #print(f"Year: {year}, Title: {films[year]}")

# .values() gives us the titles
for title in films.values():
    print(title)

#.items() gives both as a tuple (first the key, then the value)
for year, title in films.items():
                print(f"{year} was released in {title}")



