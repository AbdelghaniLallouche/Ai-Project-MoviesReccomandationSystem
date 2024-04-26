import Navbar from "./Navbar";
import { useState } from "react";

function App() {
  const movies = [
    {
      id: 1,
      name: "The Godfather",
      genre: "Drama",
      duration: "Long",
      language: "Italian",
      favActor: "pacino",
      img: "src/pics/R.png",
    },
    {
      id: 2,
      name: "The Irishman",
      genre: "Drama",
      duration: "Long",
      language: "English",
      favActor: "deniro",
      img: "src/pics/Irish.jpg",
    },
    {
      id: 3,
      name: "The Wolf of Wall Street",
      genre: "Action",
      duration: "Medium",
      language: "English",
      favActor: "dicaprio",
      img: "src/pics/wol.jpg",
    },
    {
      id: 4,
      name: "The Departed",
      genre: "Action",
      duration: "Medium",
      language: "English",
      favActor: "dicaprio",
      img: "src/pics/dep.jpg",
    },
    {
      id: 5,
      name: "Heat",
      genre: "Action",
      duration: "Long",
      language: "English",
      favActor: "pacino",
      img: "src/pics/heat.jpg",
    },
    {
      id: 6,
      name: "Scarface",
      genre: "Action",
      duration: "Long",
      language: "English",
      favActor: "pacino",
      img: "src/pics/sca.jpg",
    },
    {
      id: 7,
      name: "Casino",
      genre: "Drama",
      duration: "Long",
      language: "English",
      favActor: "deniro",
      img: "src/pics/casin.jpg",
    },
    {
      id: 8,
      name: "Goodfellas",
      genre: "Drama",
      duration: "Long",
      language: "English",
      favActor: "deniro",
      img: "src/pics/goodfellas.jpg",
    },
    {
      id: 9,
      name: "The Aviator",
      genre: "Drama",
      duration: "Long",
      language: "English",
      favActor: "dicaprio",
      img: "src/pics/av.jpg",
    },
    {
      id: 10,
      name: "Shutter Island",
      genre: "Drama",
      duration: "Medium",
      language: "English",
      favActor: "dicaprio",
      img: "src/pics/shi.jpg",
    },
  ];
  const [isSubmited, setIsSubmited] = useState(false);
  const [selectedMovies, setSelectedMovies] = useState([]);
  const [genre, setGenre] = useState("");
  const [duration, setDuration] = useState("");
  const [language, setLanguage] = useState("");
  const [favActor, setFavActor] = useState("");

  return (
    <div>
      <Navbar />
      <div className="container mx-auto mt-4">
        <h1 className="text-2xl font-bold">Welcome to MoviesRec</h1>
        <p>This is your personalized movie recommendation app.</p>

        <form className="max-w-sm mx-auto mt-8">
          <div className="mb-4">
            <label
              htmlFor="genre"
              className="block text-gray-700 font-bold mb-2"
            >
              Genre:
            </label>
            <select
              id="genre"
              name="genre"
              value={genre}
              onChange={(e) => {
                setGenre(e.target.value);
              }}
              className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500"
              required
            >
              <option value="">Select genre</option>
              {/* options for this genres Drama, Action, Comedy, Horror,ScienceFiction,Fantasy */}
              <option value="Drama">Drama</option>
              <option value="Action">Action</option>
              <option value="Comedy">Comedy</option>
              <option value="Horror">Horror</option>
              <option value="ScienceFiction">ScienceFiction</option>
              <option value="Fantasy">Fantasy</option>
              {/* Add more genre options as needed */}
            </select>
          </div>
          <div className="mb-4">
            <label
              htmlFor="duration"
              className="block text-gray-700 font-bold mb-2"
            >
              Duration:
            </label>
            <select
              id="duration"
              name="duration"
              value={duration}
              onChange={(e) => {
                setDuration(e.target.value);
              }}
              className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500"
              required
            >
              <option value="">Select duration</option>
              <option value="Old">{`[2010-2020] ==> Old`}</option>
              <option value="New">{`[2020-2024] ==> New`}</option>
              <option value="Veryold">{`<2010 ==> Veryold`}</option>
              {/* Add more duration options as needed */}
            </select>
          </div>
          <div className="mb-4">
            <label
              htmlFor="language"
              className="block text-gray-700 font-bold mb-2"
            >
              Language:
            </label>
            <select
              id="language"
              name="language"
              value={language}
              onChange={(e) => {
                setLanguage(e.target.value);
              }}
              className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500"
              required
            >
              <option value="">Select language</option>
              {/* options of this languages English , Spanish, French, Korean, Chinese, German, Russian */}
              <option value="English">English</option>
              <option value="Spanish">Spanish</option>
              <option value="French">French</option>
              <option value="Korean">Korean</option>
              <option value="Chinese">Chinese</option>
              <option value="German">German</option>
              <option value="Russian">Russian</option>
              {/* Add more language options as needed */}
            </select>
          </div>
          <div className="mb-4">
            <label
              htmlFor="favactor"
              className="block text-gray-700 font-bold mb-2"
            >
              FavActor:
            </label>
            <select
              id="favactor"
              name="favactor"
              value={favActor}
              onChange={(e) => {
                setFavActor(e.target.value);
              }}
              className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-indigo-500"
              required
            >
              <option value="">Select Favactor</option>
              <option value="pacino">Al Pacino</option>
              <option value="deniro">Robert Deniro</option>
              <option value="dicaprio">Leonardo Di Caprio</option>
              {/* Add more language options as needed */}
            </select>
          </div>
          <button
            onClick={async (e) => {
              e.preventDefault();
              const res = await fetch("http://127.0.0.1:8000/api/movie", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  language: language,
                  type: "Movie",
                  time: duration,
                  genre: genre,
                  principalactor:"KeanuReeves",
                }),
              });
              const data = await res.json();
              console.log(language, duration, genre, favActor);
              console.log(data);
            }}
            type="submit"
            className="bg-indigo-500 text-white py-2 px-4 rounded hover:bg-indigo-600 focus:outline-none focus:bg-indigo-600"
          >
            Submit
          </button>
        </form>

        {isSubmited && (
          <div className="mt-10">
            <h2 className="text-2xl font-bold">Recommended Movies : </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
