import csv
import os
from . import app, db
from .models import Episode, Guest, Appearance

def seed_database():
    with app.app_context():
        print("Seeding database...")
        
        # clear existing data
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()

        # construct path to csv file
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'seed.csv')
        print(f"Looking for seed.csv at: {csv_path}")

        # check if file exists
        if not os.path.exists(csv_path):
            print(f"Error: seed.csv not found at {csv_path}")
            return

        # read csv and seed data
        try:
            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # create or get episode
                    episode = Episode.query.filter_by(date=row['Show']).first()
                    if not episode:
                        episode = Episode(date=row['Show'], number=int(row['Show'].split('/')[0]))
                        db.session.add(episode)

                    # create or get guest
                    guest = Guest.query.filter_by(name=row['Raw_Guest_List']).first()
                    if not guest:
                        guest = Guest(name=row['Raw_Guest_List'], occupation=row['GoogleKnowlege_Occupation'])
                        db.session.add(guest)

                    # create appearance
                    appearance = Appearance(episode=episode, guest=guest, rating=3)  # default rating
                    db.session.add(appearance)

            db.session.commit()
            print("Database seeded successfully!")
        except Exception as e:
            print(f"An error occurred while seeding the database: {str(e)}")
            db.session.rollback()

if __name__ == '__main__':
    seed_database()