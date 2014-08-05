/**
 * Description:
 * Parses the raw Wikipedia dataset and outputs the network state.
 *
 * Authors: Ali Hajimirza and Jason White
 */

#include <iostream>
#include <fstream>
#include <sstream>

/**
 * Reads the view count for each article from the specified file.
 */
size_t* read_file(std::istream &f, size_t length)
{
    std::string line;

    size_t* article_views = new size_t[length];

    // Initialize article views.
    for (size_t i = 0; i < length; i++)
        article_views[i] = 0;

    // Sum up each article view count.
    size_t page_id, page_view, tmp;
    while (std::getline(f, line))
    {
        std::stringstream ss(line);
        ss >> page_id;
        ss.ignore();
        ss >> tmp;
        ss.ignore();
        ss >> page_view;
        article_views[page_id] += page_view;
    }

    return article_views;
}

/**
 * Writes the view count for each article to the specified file.
 */
void write_file(std::ostream &f, size_t* article_views, size_t length)
{
    for (size_t i = 0; i < length; i++)
        f << i << "," << article_views[i] << std::endl;
}

int main(int argc, char const *argv[])
{
    if (argc < 2)
    {
        std::cerr << "Usage: ./process usercount < view_map > graph_file" << std::endl;
        return 1;
    }

    size_t length = 0;
    std::istringstream(argv[1]) >> length;

    size_t* article_views = read_file(std::cin, length);
    write_file(std::cout, article_views, length);
    delete article_views;

    return 0;
}
