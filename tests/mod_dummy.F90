module mod_dummy
  
   implicit none

   private
  
   !=================================================
   ! module parameters
   !=================================================
   

   CONTAINS

   SUBROUTINE test_rules()
      
      character(len=100) :: p_source_name
      ! test Rule 1 - snake_case
      p_source_name = "dummy.F90"
      ! test Rule 2 - verify_file_ext
      ! test Rule 3 - verify_module_name
   
   
      ! test Rule 4 ...
      ! test Rule 5
      ! test Rule 6

   END SUBROUTINE
   

end module mod_dummy

