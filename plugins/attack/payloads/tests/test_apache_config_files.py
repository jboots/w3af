'''
test_apache_config_files.py

Copyright 2012 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''
from plugins.attack.payloads.tests.payload_test_helper import PayloadTestHelper
from plugins.attack.payloads.payload_handler import exec_payload


class test_apache_config_files(PayloadTestHelper):
    
    EXPECTED_RESULT = [ '/etc/apache2/envvars',
                        '/etc/apache2/magic',
                        '/etc/apache2/ports.conf',
                        '/etc/apache2/apache2.conf',
                        '/etc/apache2/conf.d/security']

    def test_apache_config_files(self):
        result = exec_payload(self.shell, 'apache_config_files', use_api=True)
        self.assertEquals(set(self.EXPECTED_RESULT), set(result['apache_config'].keys()))
        
