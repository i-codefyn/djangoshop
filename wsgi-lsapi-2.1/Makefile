CC=		gcc
BASECFLAGS=	-Wno-unused-result -Wsign-compare -DNDEBUG  -D_GNU_SOURCE -fPIC -fwrapv -O2 -pthread -Wno-unused-result -Wsign-compare -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -D_GNU_SOURCE -fPIC -fwrapv -D_GNU_SOURCE -fPIC -fwrapv -O2 -pthread -Wno-unused-result -Wsign-compare -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration  -D_GNU_SOURCE -fPIC -fwrapv -O2 -pthread -Wno-unused-result -Wsign-compare -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -O0 -g3
CPPFLAGS=	-I. -I/opt/alt/python310/include/python3.10
DEFINES=	
CFLAGS=		$(BASECFLAGS) $(CPPFLAGS) $(DEFINES)
LIBPL=		/opt/alt/python310/lib64/python3.10/config-3.10-x86_64-linux-gnu
LDFLAGS=	-Wl,-z,relro  -L/opt/alt/openssl11/lib64 -L/opt/alt/python310/lib64 -Wl,-rpath=/opt/alt/python310/lib64,-rpath=/opt/alt/openssl11/lib64 -Wl,--enable-new-dtags -Wl,-v -L/opt/alt/sqlite/usr/lib64 -L/opt/alt/python310/lib64 -Wl,-rpath=/opt/alt/sqlite/usr/lib64 -pthread -Wno-unused-result -Wsign-compare -ffat-lto-objects -flto-partition=none -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -Wl,-z,relro  -L/opt/alt/openssl11/lib64 -L/opt/alt/python310/lib64 -Wl,-rpath=/opt/alt/python310/lib64,-rpath=/opt/alt/openssl11/lib64 -Wl,--enable-new-dtags -Wl,-v -L/opt/alt/sqlite/usr/lib64 -L/opt/alt/python310/lib64 -Wl,-rpath=/opt/alt/sqlite/usr/lib64 -pthread -Wno-unused-result -Wsign-compare -ffat-lto-objects -flto-partition=none -g -std=c99 -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -L/opt/alt/python310/lib64
LINKFORSHARED=	-Xlinker -export-dynamic
LIBS=		-lcrypt -ldl  -lutil -lm
SYSLIBS=	-lm
VERSION=	3.10

OBJS=		main.o wsgi.o wsgiinput.o wsgiwrapper.o lsapilib.o lsapi-glue.o

all: lswsgi

lswsgi: $(OBJS)
	$(CC) $(LDFLAGS) $(LINKFORSHARED) -o $@ $(OBJS) -L$(LIBPL) -lpython$(VERSION) $(LIBS) $(SYSLIBS)

main.o: main.c  wsgi.h version.h

lsapilib.o: lsapilib.c lsapilib.h

wsgi.o: wsgi.c wsgi-int.h wsgi.h

wsgiinput.o: wsgiinput.c wsgi-int.h wsgi.h

wsgiwrapper.o: wsgiwrapper.c wsgi-int.h wsgi.h

lsapi-glue.o: lsapi-glue.c 

clean:
	rm -f lswsgi *.o core *.core

distclean: clean
	rm -f Python.framework Makefile
