import SQL_Connector

def vax_vs_nonvax():
    print("\nTotal cases and deaths by vaccinated and unvaccinated from reporting districts")
    vax_vs_nonvax_cases()
    vax_vs_nonvax_deaths()


def vax_vs_nonvax_deaths():
    sql_comm = "Select sum(Unvaccinated_outcome), sum(Vaccinated_outcome), sum(Fully_vaccinated_population), " \
               "sum(Unvaccinatedpopulation) From covid_cases_or_deaths_by_age_group_and_vaccination_status where " \
               "outcome = 'death'" \

    SQL_Connector.cursor.execute(sql_comm)
    table = SQL_Connector.cursor.fetchall()

    for row in table:
        sum_deaths = row[0] + row[1]
        print("Total Deaths = ", add_commas(sum_deaths))
        print("Unvaccinated deaths", add_commas(row[0]))
        print("Vaccinated deaths", add_commas(row[1]))
        print("Percent of Unvaccinated deaths", percentage_of(row[3], row[0]))
        print("Percent of Vaccinated deaths", percentage_of(row[2], row[1]))


def vax_vs_nonvax_cases():
    sql_comm = "Select sum(Unvaccinated_outcome), sum(Vaccinated_outcome), sum(Fully_vaccinated_population), " \
               "sum(Unvaccinatedpopulation) From covid_cases_or_deaths_by_age_group_and_vaccination_status where " \
               "outcome = 'case'" \

    SQL_Connector.cursor.execute(sql_comm)
    table = SQL_Connector.cursor.fetchall()
    for row in table:
        sum_cases = row[0] + row[1]
        print("Total Cases = ", add_commas(sum_cases))
        print("Unvaccinated cases", add_commas(row[0]))
        print("Vaccinated cases", add_commas(row[1]))
        print("Percent of Unvaccinated cases", percentage_of(row[3], row[0]))
        print("Percent of Vaccinated cases", percentage_of(row[2], row[1]))


def total_usa():
    SQL_Connector.cursor.execute('SELECT SUM(tot_cases), SUM(tot_death) FROM united_states_covid_cases_and_deaths_by_state_over_time')
    table = SQL_Connector.cursor.fetchall()
    us_pop = 331893745
    for row in table:
        print("Total Cases = ", add_commas(row[0]))
        print("Total Deaths= ", add_commas(row[1]))
        print("Percent of cases", percentage_of(us_pop, row[0]))
        print("Percent of cases leading to deaths", percentage_of(row[0], row[1]))
        print("Percent of US population that has died", percentage_of(us_pop, row[1]))


def total_state():
    sql_comm = 'Select state, tot_cases, tot_death FROM united_states_covid_cases_and_deaths_by_state_over_time ' \
               'group by state order by tot_cases desc'
    SQL_Connector.cursor.execute(sql_comm)
    table = SQL_Connector.cursor.fetchall()

    for row in table:
        print("State = ", row[0])
        print("Total Cases = ", add_commas(row[1]))
        print("Total Deaths= ", add_commas(row[2]))
        print('\n')


def percentage_of(num1, num2):
    percent = (num2 / num1) * 100
    round_per = round(percent, 2)
    return_string = '{0}%'.format(round_per)
    return return_string


def add_commas(num_no_comma):
    num_comma = "{:,}".format(num_no_comma)
    return num_comma
