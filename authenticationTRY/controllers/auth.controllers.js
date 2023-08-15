import {response} from 'express';
import Usuario from '../models/user.js';
import bcrypt from 'bcryptjs';
import generateJWT from '../helpers/generateJWT.js';

const login = async(req, res=response) => {
    const {email, password} = req.body
    try {
        /* verificamos si el email existe */
        const user = await Usuario.findOne({email})
        if(!user){
            return res.status(400).json({msg: 'El usuario no es valido'})
        }
        /* el usauario existe? */
        if(user.status == false){
            return res.status(400).json({msg: 'El usuario no esta activo'})
        } 
        /* la contraseña es correcta? */
        if(!bcrypt.compareSync(password, user.password)){
            /* la funcion arriba es para verificar la contraseña de el req y la que viene en la base de datos */
            return res.status(400).json({msg: 'La contraseña no es valida'})
        }
        
        /* validacion de json web token */
        const token = await generateJWT(user.id)
    
        res.json({
            user,
            token
        })
    } catch (error) {
        console.log(error)
        return res.json({msg: "error contacte con soporte tecnico"})    
    }
  
}

export const auth = {
    login
}