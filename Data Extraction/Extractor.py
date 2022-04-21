from tmdbv3api import TMDb
from tmdbv3api import Discover, Movie
from datetime import datetime, timedelta
import csv


def get_data_id(movie_id):
    movie = Movie()
    movie.api_key = 'd32b24227485bb855585fe208dd42664'
    movie.language = 'en-US'
    data = movie.details(movie_id)
    print(str(data).encode('utf-8'))
    return data


def get_data(page_no, date):
    discover = Discover()
    discover.api_key = 'd32b24227485bb855585fe208dd42664'

    discover.language = 'en'
    discover.debug = True
    movie = discover.discover_movies({
        'primary_release_date.gte': date,
        'primary_release_date.lte': date,
        'page': page_no,
    })
    return movie

# awk '!seen[$0]++' final.csv > temp.csv
#2009-12-31
#2015-10-28

datetime_object = datetime.strptime('1980-01-01', '%Y-%m-%d')
header = ['adult', 'casts', 'video', 'videos', 'tagline', 'status', 'spoken_languages', 'runtime',
          'production_companies', 'production_countries', 'budget', 'revenue', 'backdrop_path', 'genre_ids', 'genres',
          'id', 'original_language', 'original_title', 'overview',
          'popularity', 'poster_path', 'release_date', 'release_dates', 'title', 'video', 'vote_average', 'vote_count']
with open('data/data.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for i in range(0, 3650):
        print("Current index: ", i)
        datetime_object = datetime_object + timedelta(days=1)
        string_date = datetime_object.strftime('%Y-%m-%d')
        print(string_date)

        page_index = 1
        while True:
            data = None
            try:

                data = get_data(page_index, string_date)
            except Exception as e:
                print(e)
                pass

            if len(data) <= 0:
                break

            if data is not None:

                print(len(data))
                print(data[0].keys())

                page_index += 1

                for movie in data:
                    # movie.pop('genre_ids', None)

                    passed = True
                    while(passed):
                        m_id = movie['id']
                        movie_data = None
                        try:

                            movie_data = get_data_id(m_id)
                        except:
                            pass
                        if movie_data is not None:
                            movie['genres'] = [str(i['name']).replace(',',' ') for i in movie_data['genres']]
                            movie['budget'] = movie_data['budget']
                            movie['production_companies'] = [str(i['name']).replace(',',' ') for i in movie_data['production_companies']]
                            movie['production_countries'] = [str(i['name']).replace(',',' ') for i in movie_data['production_countries']]
                            movie['revenue'] = movie_data['revenue']
                            movie['runtime'] = movie_data['runtime']
                            movie['spoken_languages'] = [str(i['english_name']).replace(',',' ') for i in movie_data['spoken_languages']]
                            movie['status'] = movie_data['status'].replace(',',' ')
                            movie['tagline'] = movie_data['tagline'].replace(',',' ')
                            movie['video'] = movie_data['video']
                            movie['videos'] = movie_data['videos']
                            movie['casts'] = [str(i['name']).replace(',',' ') for i in movie_data['casts']['cast']]
                            # movie['keywords'] = movie_data['keywords'].replace(',',' ')
                            movie['release_dates'] = movie_data['release_dates']
                            writer.writerow(movie)
                            passed = False
