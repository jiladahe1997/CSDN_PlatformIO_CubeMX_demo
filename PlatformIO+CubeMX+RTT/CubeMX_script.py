Import("env")

env.Prepend(LINKFLAGS=[
  "--specs=nosys.specs"
])