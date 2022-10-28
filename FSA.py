class FSA:
    """A Forward Sortation Area (FSA), a geographic area defined by the first 3 digits of your
    postal code. A lot of COVID-19 data is broken down this way, as it is a nice indicator of your
    neighboorhood and general area in the city. This datatype stores all the data I track for each
    FSA.
    """
    # Instance attributes:
    # - name: Name of the FSA, in the format A1A, where A is a letter and 1 is a number
    # - number_of_restaurants: The number of restaurants in the FSA
    # - number_or_minor_infractions: The total number of minor infractions the restaurants in this
    #   FSA have incurred
    # - number_of_significant_infractions: The total number of significant infractions the
    #   restaurants in this FSA have incurred
    # - number_of_crucial_infractions: The total number of crucial infractions the restaurants in
    #   this FSA have incurred
    # - total_covid_cases_per_100: The total COVID-19 Cases  in this FSA, per 100 people
    # - total_covid_hospitalizations_per_1000: Total hospitalizations due to COVID-19 in this FSA,
    #   per 1000 people
    # - total_covid_deaths_per_1000: Total deaths due to COVID-19 in this FSA, per 1000 people
    # - population: The population (as of the 2016 Census) in this FSA
    # - percent_1_dose: The percentage of people who have AT LEAST 1 dose of vaccine in this FSA
    # - percent_2_doses: The percentage of people who have AT LEAST 2 doses of vaccine in this FSA
    name: str
    number_of_restaurants: int
    number_of_minor_infractions: int
    number_of_significant_infractions: int
    number_of_crucial_infractions: int
    total_covid_cases_per_100: float
    total_covid_hospitalizations_per_1000: float
    total_covid_deaths_per_1000: float
    population: int
    percent_1_dose: float
    percent_2_doses: float

    def __init__(self, fsa_name) -> None:
        self.name = fsa_name
        self.number_of_restaurants = 0
        self.number_of_minor_infractions = 0
        self.number_of_significant_infractions = 0
        self.number_of_crucial_infractions = 0
        self.total_covid_cases_per_100 = -1.0  # Defaults to -1.0 since this data can be suppressed.
        # This way, easy to pick out of graphs and avoid weird weightings.
        self.total_covid_hospitalizations_per_1000 = -1.0
        self.total_covid_deaths_per_1000 = -1.0
        self.population = 0
        self.percent_1_dose = 0.0
        self.percent_2_doses = 0.0
