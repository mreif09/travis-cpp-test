#include "gtest/gtest.h"
#include "src.hpp"

TEST(SRC, add) {
  EXPECT_EQ(add(1, 2), 3);
}
