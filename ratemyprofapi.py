import ratemyprofessor

professor = ratemyprofessor.get_professor_by_school_and_name(
ratemyprofessor.get_school_by_name("University of Toronto St. George Campus"), "S cohen")
if professor is not None:
    print("%sworks in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
    print("Rating: %s / 5.0" % professor.rating)
    print("Difficulty: %s / 5.0" % professor.difficulty)
    print("Total Ratings: %s" % professor.num_ratings)
    professorid = professor.id
    link_url = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid="
    print(link_url +  str(professorid))

    for course in professor.courses:
        print(course.name + "\n")
    if professor.would_take_again is not None:
        print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
    else:
        print("Would Take Again: N/A")

    
    print(ratemyprofessor.get_school_by_name("University of Toronto St. George Campus").name)