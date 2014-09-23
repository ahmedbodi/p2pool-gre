#include <stdint.h>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/uniform_int.hpp>

static const int64_t COIN = 100000000;

int64_t static GetBlockBaseValue(int nHeight)
{
	int64_t nSubsidy = 2000 * COIN;
	nSubsidy >>= (nHeight / 2500000);
	//GreenCoin Subsidy payment
	for (int x = 0; x < (nHeight / 25000000); x++)
		nSubsidy = nSubsidy * 1 / 2;
	return nSubsidy;
}

using namespace boost::python;
BOOST_PYTHON_MODULE(gre_subsidy)
{
    def("GetBlockBaseValue", GetBlockBaseValue);
}
