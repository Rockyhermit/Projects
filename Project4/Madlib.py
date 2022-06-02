
to_email = input("To Email: ")
applying_post = input("Post your Applying for: ")
job_website = input("Job applying website: ")
to_name = input("To Name: ")
degree = input("Your Degree [Bachelors/Masters]")
university = input("University you got your Degree: ")
exprerience_years = input("Work Experience [in years] = ")
previous_position = input("Previous Position: ")
previous_company = input("Previous Company: ")
work_expirence_includes = input("Your work expirience includes: ")
Name = input("Your Name:")
number = input("Your Contact Number: ")
your_email = input("Your email: ")


madlib = f'''
To: {to_email}

Subject: Application for {applying_post} with {job_website}

Dear {to_name},

This is regarding your call for a {applying_post} on the Indeed job portal. I have reviewed the job requirements and visited the {job_website} website, and I am interested in working with you.

I have a first-class {degree} from {university}, and I have worked for {exprerience_years} as a {previous_position} with {previous_company}. My work experience includes {work_expirence_includes}. As a result of these, we were successful in seeing higher sales for five years in a row. Given my understanding and passion, I believe I will be a good fit for the position in your company.

Please see my attached resume and work samples.

Thank you for taking the time to consider my application.

I hope to hear from you.

Best regards,

{Name}

+91-{number}

{your_email}'''
print(madlib)