#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <ctime>

// Default length of the map file
unsigned int LENGTH = 15148210;

unsigned int* read_file(std::string& path, int length)
{
	std::cout << "Reading the file: " << path << std::endl;
	std::ifstream infile(path.c_str());
	std::string line;
	unsigned int* article_views = new unsigned int[length];
	for (int i=0; i < length; i++)
	{
		article_views[i] = 0;
	}
	unsigned int page_id, page_view, tmp;
	while (std::getline(infile, line))
	{
		std::stringstream ss(line);
		ss >> page_id;
		ss.ignore();
		ss >> tmp;
		ss.ignore();
		ss >> page_view;
		article_views[page_id] += page_view;
   	}
   	infile.close();
   	return article_views;
}

void write_file(std::string& path, unsigned int* article_views, int length)
{
	std::cout << "Writing to file: " << path << std::endl;
	std::ofstream outputFile;
	outputFile.open(path.c_str());
	for (int i=0; i < length; i++)
	{
		outputFile << i << "," << article_views[i] << std::endl;
	}
	outputFile.close();
}

int file_length(std::string& map_file_path)
{
	std::cout << "Counting the number of articles..." << std::endl;
	std::ifstream infile(map_file_path.c_str());
	std::string line;
	int num_pages = 0;
	std::string tmp;
	while (std::getline(infile, line))
	{
		std::stringstream ss(line);
		ss >> tmp;
		ss >> num_pages;
   	}
    return num_pages;
}

int main(int argc, char const *argv[])
{
	if (argc < 2)
		std::cout << "No file specified." << std::endl;
	for (int i=1; i < argc; i++)
	{
		if (std::strncmp(argv[i], "--map-file", 10) == 0)
		{
			std::string map_file_path = std::string(argv[i + 1]);
			LENGTH = file_length(map_file_path);
			std::cout << "The length was set to " << LENGTH << std::endl;
			break;
		}
	}

	for (int i=1; i < argc; i++)
	{
		if (std::strncmp(argv[i], "--map-file", 10) == 0)
		{
			i++;
			continue;
		}
		std::string input_file_path = std::string(argv[i]);
		unsigned int* article_views = read_file(input_file_path,LENGTH);
		int lastindex = input_file_path.find_last_of('.'); 
		std::string output_file_path = input_file_path.substr(0, lastindex) + ".data"; 
		write_file(output_file_path, article_views, LENGTH);
		delete article_views;
	}

	return 0;
}
