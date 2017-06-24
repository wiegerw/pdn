// Copyright: Wieger Wesselink 2011
//
// Distributed under the Boost Software License, Version 1.0.
// http://www.boost.org/LICENSE_1_0.txt

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#include <stdexcept>
#include "dparse.h"

extern D_ParserTables parser_tables_fen;

struct dparser
{
  D_Parser* m_parser;
  D_ParserTables& m_table;

  dparser(D_ParserTables& table)
    : m_table(table)
  {
    m_parser = new_D_Parser(&table, 0);
    m_parser->initial_globals = this;
    m_parser->save_parse_tree = 1;
    m_parser->initial_scope = NULL;
  }

  ~dparser()
  {
    free_D_Parser(m_parser);
  }

  void parse(const std::string& text)
  {
    D_ParseNode* result = dparse(m_parser, const_cast<char*>(text.c_str()), text.size());
    if (!result || m_parser->syntax_errors)
    {
      throw std::exception();
    }
  }
};

void parse(const std::string& s)
{
  try
  {
    dparser p(parser_tables_fen);
    p.parse(s);
    std::cout << "Parsing succeeded." << std::endl;
  }
  catch (std::exception& e)
  {
    std::cout << "Parsing failed." << std::endl;
  }
}

std::string read_text(std::istream& from)
{
  std::ostringstream out;
  std::string s;
  while (std::getline(std::cin, s))
  {
    out << s << std::endl;
  }
  return out.str();
}

int main(int argc, char *argv[])
{
  std::string text;
  std::string filename;

  if (argc > 1)
  {
    filename = std::string(argv[1]);
  }

  if (!filename.empty())
  {
    std::ifstream from(filename.c_str());
    text = read_text(from);
  }
  else
  {
    text = read_text(std::cin);
  }
  parse(text);

  return 0;
}
