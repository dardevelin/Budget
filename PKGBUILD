# Maintainer: Marc Thomas <mat at mthx dot org>
pkgname=budget-git
pkgver=0.1
pkgrel=1
pkgdesc="Personal finance application built for the Gnome desktop (alpha version)"
arch=('i686' 'x86_64')
url="https://github.com/mthxx/Budget"
license=('GPL2')
install= budget.install
source=(git://github.com/mthxx/Budget)
sha256sums=() #autofill using updpkgsums
md5sums=('SKIP')

build() {
  cd "$pkgname-$pkgver"

  ./configure --prefix=/usr
  make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir/" install
}
