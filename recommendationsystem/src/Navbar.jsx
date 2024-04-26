// Navbar.js

function Navbar() {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white font-bold text-xl">MoviesRec</div>
        <ul className="flex space-x-4 text-white">
          <li>
            <a href="/" className="hover:text-gray-300">Home</a>
          </li>
          {/* Add more nav items here */}
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
