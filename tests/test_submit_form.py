from model.helpers import app
from model.user import User

user = User(
    first_name='Daniil',
    last_name='M',
    email='test@mail.ru',
    gender='Male',
    mobile_number='1234567890',
    date_of_birth='15 August,1989',
    subjects=["Computer Science", "English"],
    hobbies=['Sports', 'Reading', 'Music'],
    photo='fry.jpeg',
    current_address='Love street',
    state='NCR',
    city='Delhi'
)


def test_submit_form(init):
    app.form.set_first_name(user.first_name)
    app.form.set_last_name(user.last_name)
    app.form.set_email(user.email)
    app.form.set_gender(user.gender)
    app.form.set_mobile_number(user.mobile_number)
    app.form.set_date_of_birth(user.date_of_birth)
    app.form.set_subjects(user.subjects)
    app.form.subjects_should_have(user.subjects)
    app.form.set_hobbies(user.hobbies)
    app.form.set_photo(user.photo)
    app.form.set_current_address(user.current_address)
    app.form.set_state(user.state)
    app.form.set_city(user.city)
    app.form.submit()
    app.result.verify_sent_data(user.full_name(user.first_name, user.last_name),
                                user.email,
                                user.gender,
                                user.mobile_number,
                                user.date_of_birth,
                                user.subjects,
                                user.hobbies,
                                user.photo,
                                user.current_address,
                                user.state_and_city(user.state, user.city))