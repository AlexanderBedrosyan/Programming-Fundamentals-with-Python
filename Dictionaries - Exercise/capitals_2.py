class GetStatistics():

    def __init__(self, countries_list, capitals_list):
        self.capitals_list = capitals_list
        self.countries_list = countries_list

    def create_statistics_dictionary(self):
        statistics_dictionary = {country: capital for country, capital in zip(self.countries_list, self.capitals_list)}
        return statistics_dictionary

    def __repr__(self):
        final_result = []
        for country, capital in self.create_statistics_dictionary().items():
            final_result.append(f"{country} -> {capital}")
        return '\n'.join(final_result)


countries = [ch for ch in input().split(", ")]
capitals = [ch for ch in input().split(", ")]
print(GetStatistics(countries, capitals))
