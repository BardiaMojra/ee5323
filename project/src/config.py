''' config module
'''
import os

class config(object):
  def __init__(self, TEST_ID, OUT_DIR, output_labels, cart_mass, cart_size,
               pend_1_length, pend_1_mass, pend_1_moment, pend_1_radius,
               pend_2_length, pend_2_mass, pend_2_moment, pend_2_radius,
               K, Nbar):
    self.config = {'TEST_ID':TEST_ID,
                   'OUT_DIR':OUT_DIR,
                   'output_labels':output_labels,
                   'cart_mass':cart_mass,
                   'cart_size':cart_size,
                   'pend_1_length':pend_1_length,
                   'pend_1_mass':pend_1_mass,
                   'pend_1_moment':pend_1_moment,
                   'pend_1_radius':pend_1_radius,
                   'pend_2_length':pend_2_length,
                   'pend_2_mass':pend_2_mass,
                   'pend_2_moment':pend_2_moment,
                   'pend_2_radius':pend_2_radius,
                   'K':K,
                   'Nbar':Nbar}
  def log_config(self):
    path = self.config['OUT_DIR']
    test_id = self.config['TEST_ID']
    f_path  = path+test_id+'_config.log'
    if os.path.exists(f_path):
      os.remove(f_path)
    with open(f_path, 'w') as output_file:
      print(self.config, file=output_file)
      output_file.close()
    return



# EOF
