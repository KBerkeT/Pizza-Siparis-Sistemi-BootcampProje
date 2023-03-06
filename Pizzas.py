class Pizza:
  """
  Pizza sınıfı herhangi bir değer almaz.
  Aşağıdaki özellikleri içerir:
    description: Pizzanın tanımı - içindeki malzemeler
    cost: Pizzanın ücreti

  Pizza sınıfının get_description() ve get_cost() adında iki işlevi vardır.
    get_description(): Pizza sınıfının description özelliğini return eder.
    get_cost(): Pizza sınıfının cost özelliğini return eder.
  
  """
  description = "İnce hamur, mozarella peyniri"
  cost = 50

  # get_description işlevi description özelliğini return eder.
  def get_description(self):
    """
    Pizza sınıfının description özelliğini return eder.
    """
    return self.description

  # get_cost işlevi cost özelliğini return eder.
  def get_cost(self):
    """
    Pizza sınıfının description özelliğini return eder.
    """
    return self.cost
  
class Margherita(Pizza):
  """
  Margherita sınıfı pizza sınıfının özelliklerini miras alır.
  Aşağıdaki özellikleri içerir:
    name: Pizza adı
    description: Pizzanın tanımı - içindeki malzemeler
    cost: Pizzanın ücreti

  Margherita sınıfının get_description() ve get_cost() adında iki işlevi vardır.
    get_description(): Margherita sınıfının description özelliğini return eder.
    get_cost(): Margherita sınıfının cost özelliğini return eder.
  
  """
  name = "Margherita Pizza"

class MixPizza(Pizza):
  """
  MixPizza sınıfı pizza sınıfının özelliklerini miras alır.
  Aşağıdaki özellikleri içerir:
    name: Pizza adı
    description: Pizzanın tanımı - içindeki malzemeler
    cost: Pizzanın ücreti

  MixPizza sınıfının get_description() ve get_cost() adında iki işlevi vardır.
    get_description(): Margherita sınıfının description özelliğini return eder.
    get_cost(): Margherita sınıfının cost özelliğini return eder.
  
  """
  name = "Karışık Pizza"
  description = "İnce hamur, mozarella peyniri , sucuk, sosis, zeytin, biber, mısır"
  cost = 70

class TurkPizza(Pizza):
  """
  TurkPizza sınıfı pizza sınıfının özelliklerini miras alır.
  Aşağıdaki özellikleri içerir:
    name: Pizza adı
    description: Pizzanın tanımı - içindeki malzemeler
    cost: Pizzanın ücreti

  TurkPizza sınıfının get_description() ve get_cost() adında iki işlevi vardır.
    get_description(): Margherita sınıfının description özelliğini return eder.
    get_cost(): Margherita sınıfının cost özelliğini return eder.
  
  """
  name = "Türk Pizza"
  description = "İnce hamur, mozarella peyniri, pastırma, sucuk, biber, soğan"
  cost = 75

class ChickenPizza(Pizza):
  """
  ChickenPizza sınıfı pizza sınıfının özelliklerini miras alır.
  Aşağıdaki özellikleri içerir:
    name: Pizza adı
    description: Pizzanın tanımı - içindeki malzemeler
    cost: Pizzanın ücreti

  ChickenPizza sınıfının get_description() ve get_cost() adında iki işlevi vardır.
    get_description(): Margherita sınıfının description özelliğini return eder.
    get_cost(): Margherita sınıfının cost özelliğini return eder.
  
  """
  name = "Kıymalı Pizza"
  description = "İnce hamur, mozarella peyniri, tavuk, domates, biber"
  cost = 65

class MushroomPizza(Pizza):
  """
  MushroomPizza sınıfı pizza sınıfının özelliklerini miras alır.
  Aşağıdaki özellikleri içerir:
    name: Pizza adı
    description: Pizzanın tanımı - içindeki malzemeler
    cost: Pizzanın ücreti

  MushroomPizza sınıfının get_description() ve get_cost() adında iki işlevi vardır.
    get_description(): Margherita sınıfının description özelliğini return eder.
    get_cost(): Margherita sınıfının cost özelliğini return eder.
  
  """
  name = "Mantarlı Pizza"
  description = "İnce hamur, mozarella peyniri, zeytin, mantar"
  cost = 60

class SausagePizza(Pizza):
  """
  SausagePizza sınıfı pizza sınıfının özelliklerini miras alır.
  Aşağıdaki özellikleri içerir:
    name: Pizza adı
    description: Pizzanın tanımı - içindeki malzemeler
    cost: Pizzanın ücreti

  SausagePizza sınıfının get_description() ve get_cost() adında iki işlevi vardır.
    get_description(): Margherita sınıfının description özelliğini return eder.
    get_cost(): Margherita sınıfının cost özelliğini return eder.
  
  """
  name = "Sucuklu Pizza"
  description = "İnce hamur, mozarella peyniri, sucuk"
  cost = 55


class Sauce(Pizza):
  """
  Sauce sınıfı Pizza sınıfından miras alır.
  Sauce nesnesi oluşturulurken bir component değeri alır.
    component: Bir pizza nesnesidir.
  
  Aşağıdaki özellikleri içerir:
    description: Sosun tanımı, adı
    cost: Sosun ücreti

  Sauce sınıfının get_description() ve get_cost() adında iki işlevi vardır.
  Bu işlevlerin Pizza sınıfında bulunan aynı işlevlerden farkı vardır.
  Bu işlevler Sauce nesnesi oluşturmak için kullanılan Pizza nesnesini kullanır.
    get_description(): Pizza nesnesinin description özelliğini ve Pizza  
                       sınıfından miras alınan get_description() işlevini 
                       birleştirip return eder.
    get_cost():        Pizza nesnesinin cost özelliğini ve Pizza  
                       sınıfından miras alınan get_cost() işlevini 
                       toplayıp, toplam ücreti return eder.
  """
  def __init__(self, component):
    self.component = component

  # Bu işlev sınıf oluşturulurken kullanılan pizza nesnesinin ücreti ile Sauce 
  # sınıfının ücretini toplar.
  def get_cost(self):
    """
    Pizza nesnesinin ücreti ile Sauce sınıfının ücretini toplar.
    """
    return self.component.get_cost() + super().get_cost()

  # Bu işlev sınıf oluşturulurken kullanılan Pizza nesnesinin tanımı ile Sauce 
  # sınıfının tanımını birleştirir.
  def get_description(self):
    """
    Pizza nesnesinin tanımı ile Sauce sınıfının tanımını birleştirir.
    """
    return self.component.get_description() + ", " + super().get_description()

class Ketchup(Sauce):
  """
  Sauce sınıfını miras alır ve onun işlevlerine sahiptir.
  Ketchup nesnesi oluşturulurken bir component değeri alır.
    component: Bir pizza nesnesidir.
  
  Aşağıdaki özellikleri içerir:
    description: Sosun tanımı, adı
    cost: Sosun ücreti
  """
  description = "ketçap"
  cost = 5

class Mayonnaise(Sauce):
  """
  Sauce sınıfını miras alır ve onun işlevlerine sahiptir.
  Mayonnaise nesnesi oluşturulurken bir component değeri alır.
    component: Bir pizza nesnesidir.
  
  Aşağıdaki özellikleri içerir:
    description: Sosun tanımı, adı
    cost: Sosun ücreti
  """  
  description = "mayonez"
  cost = 5  

class BBQ(Sauce):
  """
  Sauce sınıfını miras alır ve onun işlevlerine sahiptir.
  BBQ nesnesi oluşturulurken bir component değeri alır.
    component: Bir pizza nesnesidir.
  
  Aşağıdaki özellikleri içerir:
    description: Sosun tanımı, adı
    cost: Sosun ücreti
  """
  description = "BBQ sos"
  cost = 8

class Mustard(Sauce):
  """
  Sauce sınıfını miras alır ve onun işlevlerine sahiptir.
  Mustard nesnesi oluşturulurken bir component değeri alır.
    component: Bir pizza nesnesidir.
  
  Aşağıdaki özellikleri içerir:
    description: Sosun tanımı, adı
    cost: Sosun ücreti
  """
  description = "hardal"
  cost = 6

class HotSauce(Sauce):
  """
  Sauce sınıfını miras alır ve onun işlevlerine sahiptir.
  HotSauce nesnesi oluşturulurken bir component değeri alır.
    component: Bir pizza nesnesidir.
  
  Aşağıdaki özellikleri içerir:
    description: Sosun tanımı, adı
    cost: Sosun ücreti
  """
  description = "acı sos"
  cost = 6

class RanchSauce(Sauce):
  """
  Sauce sınıfını miras alır ve onun işlevlerine sahiptir.
  RanchSauce nesnesi oluşturulurken bir component değeri alır.
    component: Bir pizza nesnesidir.
  
  Aşağıdaki özellikleri içerir:
    description: Sosun tanımı, adı
    cost: Sosun ücreti
  """  
  description = "ranch sos"
  cost = 8

class Spice(Sauce):
  """
  Sauce sınıfını miras alır ve onun işlevlerine sahiptir.
  Spice nesnesi oluşturulurken bir component değeri alır.
    component: Bir pizza nesnesidir.
  
  Aşağıdaki özellikleri içerir:
    description: Sosun tanımı, adı
    cost: Sosun ücreti
  """  
  description = "baharat"
  cost = 9

